import socket
import threading

active_clients = set()
user_credentials = {}

def read_user_credentials():
    with open('users.txt', 'r') as file:
        for line in file:
            username, password = line.strip().split()
            user_credentials[username] = password

def broadcast(message, sender_socket):
    for client_socket in active_clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode())
            except:
                # Handle any errors that occur when sending the message
                pass

def handle_client(client_socket):
    client_socket.send("Введіть ваше ім'я користувача: ".encode())
    username = client_socket.recv(1024).decode().strip()

    client_socket.send("Введіть ваш пароль: ".encode())
    password = client_socket.recv(1024).decode().strip()

    if username in user_credentials and user_credentials[username] == password:
        client_socket.send("Успішний вхід!".encode())
        active_clients.add(client_socket)
        broadcast(f"{username} приєднався до чату.", client_socket)
    else:
        client_socket.send("Вхід не вдалий. Невірні облікові дані.".encode())
        return

    while True:
        message = client_socket.recv(1024).decode()
        if message.lower() == 'вийти':
            break

        broadcast(f"{username}: {message}", client_socket)

    active_clients.remove(client_socket)
    broadcast(f"{username} залишив чат.", client_socket)
    client_socket.send("До побачення!".encode())
    client_socket.close()

def main():
    read_user_credentials()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8073))
    server_socket.listen(5)
    print("Сервер чату запущено.")

    while True:
        client_socket, address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
