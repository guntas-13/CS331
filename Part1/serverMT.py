import socket
import threading

def process_task(task):
    """Process the client's task."""
    try:
        choice, data = task.split(":", 1)
        choice = int(choice)

        if choice == 1:
            return data.swapcase()
        elif choice == 2:
            return str(eval(data))
        elif choice == 3:
            return data[::-1]
        elif choice == 4:  # Exit
            return "Goodbye!"
        else:
            return "Invalid choice."
    except Exception as e:
        return f"Error processing task: {e}"

def handle_client(conn, addr):
    """Handles a single client in a separate thread."""
    print(f"[+] New connection from {addr}")

    while True:
        try:
            data = conn.recv(1024).decode()
            if not data:
                print(f"[-] Client {addr} disconnected.")
                break

            print(f"[{addr}] Received: {data}")
            response = process_task(data)
            conn.sendall(response.encode())

            if response == "Goodbye!":
                print(f"[-] Closing connection with {addr}")
                break
        except Exception as e:
            print(f"[!] Error with client {addr}: {e}")
            break

    conn.close()

def main():
    HOST = "127.0.0.1"
    PORT = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)  # CHECK THIS!

    print(f"[*] Server is running on {HOST}:{PORT}...")

    try:
        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            client_thread.start()
    except KeyboardInterrupt:
        print("\n[!] Server shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
