import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print(message)
        except:
            # Handle any errors that occur when receiving messages
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8073))

    response = client_socket.recv(1024).decode()
    print(response)

    if response == "Введіть ваше ім'я користувача: ":
        username = input("Ім'я користувача: ")
        client_socket.send(username.encode())

    response = client_socket.recv(1024).decode()
    print(response)

    if response == "Введіть ваш пароль: ":
        password = input("Пароль: ")
        client_socket.send(password.encode())

    login_status = client_socket.recv(1024).decode()
    print(login_status)

    if login_status == "Успішний вхід!":
        print("Ви тепер у чаті.")
        print("Напишіть 'вийти', щоб залишити чат.")

        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        while True:
            message = input("Ви: ")
            client_socket.send(message.encode())

            if message.lower() == 'вийти':
                break

        farewell = client_socket.recv(1024).decode()
        print(farewell)

    client_socket.close()

if __name__ == "__main__":
    main()
