import socket
import threading

def read_user_credentials():
    user_credentials = {}
    with open('users.txt', 'r') as file:
        for line in file:
            username, password = line.strip().split()
            user_credentials[username] = password
    return user_credentials

def handle_client(client_socket):
    user_credentials = read_user_credentials()

    client_socket.send("Введіть ваше ім'я користувача: ".encode())
    username = client_socket.recv(1024).decode().strip()

    client_socket.send("Введіть ваш пароль: ".encode())
    password = client_socket.recv(1024).decode().strip()

    if username in user_credentials and user_credentials[username] == password:
        client_socket.send("Успішний вхід!".encode())
        print(f"Користувач {username} увійшов в чат.")
        # Реалізуйте логіку чату для авторизованого користувача
    else:
        client_socket.send("Вхід не вдалий. Невірні облікові дані.".encode())
        return

    while True:
        message = client_socket.recv(1024).decode()
        if message.lower() == 'вийти':
            break
        print(f"{username}: {message}")
        # Реалізуйте логіку обробки повідомлень у чаті

    print(f"Користувач {username} вийшов з чату.")
    client_socket.send("До побачення!".encode())
    client_socket.close()

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8099))
    server_socket.listen(5)
    print("Сервер чату запущено.")

    while True:
        client_socket, address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
