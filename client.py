import socket

# Створення сокету клієнта
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Підключення до сервера за IP-адресою та портом
client_socket.connect(('127.0.0.1', 8080))

print("Connected to the server.")

while True:
    # Введення повідомлення для відправки серверу
    message = input("You: ")

    # Надсилання повідомлення на сервер
    client_socket.send(message.encode())

    # Перевірка, чи клієнт не хоче завершити розмову
    if message.lower() == 'exit':
        break

    # Очікування отримання відповіді від сервера
    response = client_socket.recv(1024).decode()

    # Виведення отриманої відповіді
    print(f"Server: {response}")

# Повідомлення про завершення розмови
print("Conversation ended.")

# Закриття з'єднання з сервером
client_socket.close()