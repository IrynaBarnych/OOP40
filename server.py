# server.py
import socket
import threading
import os

def handle_client(client_socket):
    filename = client_socket.recv(1024).decode()
    print(f"Отримано запит на відправку файлу: {filename}")

    if os.path.isfile(filename):
        client_socket.send("Файл існує. Хочете його отримати? (так/ні)".encode())
        response = client_socket.recv(1024).decode()

        if response.lower() == "так":
            client_socket.send("готово".encode())
            with open(filename, 'rb') as file:
                data = file.read(1024)
                while data:
                    client_socket.send(data)
                    data = file.read(1024)
            print(f"Файл успішно відправлено клієнту {client_socket.getpeername()}.")
        else:
            client_socket.send("Відмовлено у передачі файлу.".encode())
    else:
        client_socket.send("Файл не існує.".encode())

    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8093))
    server_socket.listen(5)
    print("Очікування підключень...")

    while True:
        client_socket, address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
