import socket
import threading

# Створення сокету сервера
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Прив'язка серверного сокету до IP-адреси та порту
server_socket.bind(("127.0.0.1", 8080))

# Чекаємо підключення клієнта
server_socket.listen(5)
print("Чекаємо з'єднання...")

# Функція для обробки запитів клієнта
def handle_client(client_socket, address):
    print(f"Підключення з {address} було створене!")

    while True:
        message = client_socket.recv(1024).decode()

        # Перевірка, чи клієнт не хоче завершити розмову
        if message.lower() == 'exit':
            break

        # Виведення отриманого повідомлення
        print(f"{address}: {message}")

        # Відправка відповіді клієнту
        response = input("Ви: ")
        client_socket.send(response.encode())

    print("Клієнт відвалився")
    client_socket.close()

# Очікування нових підключень
while True:
    client_socket, address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
