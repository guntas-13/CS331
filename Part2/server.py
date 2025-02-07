import socket
import time

def process_task(data):
    """Reverse the string after a 3-second delay."""
    time.sleep(3)  # Simulating delay
    return data[::-1]  # Reverse the string

def main():
    HOST = "127.0.0.1"
    PORT = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(100)

    print(f"Server is running on {HOST}:{PORT}...")

    try:
        while True:
            print("Waiting for a client to connect...")
            conn, addr = server_socket.accept()
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

            conn.close()
            print(f"Connection closed with {addr}")

    except KeyboardInterrupt:
        print("\nServer shutting down...")
    finally:
        server_socket.close()

if __name__ == "__main__":
    main()
