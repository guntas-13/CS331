import socket

def main():
    HOST = "127.0.0.1"  # Server IP
    PORT = 8080         # Server Port
    message = "!revreS ,olleH"  # Predefined string to send

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            s.sendall(message.encode())  # Send the string to the server
            
            response = s.recv(1024).decode()  # Receive the response
            print(f"Server response: {response}")

        except ConnectionRefusedError:
            print("Failed to connect to the server. Ensure it's running.")
        except KeyboardInterrupt:
            print("\nClient exiting...")

if __name__ == "__main__":
    main()
