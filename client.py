import socket
import asyncio

async def receive_messages(client_socket):
    while True:
        try:
            message = (await client_socket.recv(1024)).decode()
            print(message)
        except:
            break

async def send_messages(client_socket):
    while True:
        message = input("Ви: ")
        await client_socket.send(message.encode())

        if message.lower() == 'вийти':
            break

async def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8099))

    response = (await client_socket.recv(1024)).decode()
    print(response)

    if response == "Введіть ваше ім'я користувача: ":
        username = input("Ім'я користувача: ")
        await client_socket.send(username.encode())

    response = (await client_socket.recv(1024)).decode()
    print(response)

    if response == "Введіть ваш пароль: ":
        password = input("Пароль: ")
        await client_socket.send(password.encode())

    login_status = (await client_socket.recv(1024)).decode()
    print(login_status)

    if login_status == "Успішний вхід!":
        print("Ви тепер у чаті.")
        print("Напишіть 'вийти', щоб залишити чат.")

        asyncio.create_task(receive_messages(client_socket))
        await send_messages(client_socket)

        farewell = (await client_socket.recv(1024)).decode()
        print(farewell)

    client_socket.close()

if __name__ == "__main__":
    asyncio.run(main())
