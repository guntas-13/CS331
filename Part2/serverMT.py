import socket
import time
import threading

def process_task(data):
    """Reverse the string after a 3-second delay."""
    time.sleep(3)  # Simulating delay
    return data[::-1]  # Reverse the string

def handle_client(conn, addr):
    """Handle an individual client connection in a separate thread."""
    print(f"TCP connection established with {addr}")
    
    try:
        data = conn.recv(1024).decode()
        if not data:
            print(f"Client {addr} disconnected.")
        else:
            print(f"Received from {addr}: {data}")

            response = process_task(data)  # Reverse string with delay
            conn.sendall(response.encode())

    except Exception as e:
        print(f"Error handling client {addr}: {e}")
    
    finally:
        conn.close()
        print(f"Connection closed with {addr}")

def main():
    HOST = "127.0.0.1"
    PORT = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(100)

    print(f"Multi-Threaded Server is running on {HOST}:{PORT}...")

    try:
        while True:
            print("Waiting for a client to connect...")
            conn, addr = server_socket.accept()

            # Create a new thread for each client
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
