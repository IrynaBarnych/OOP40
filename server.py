import socket

# Створення сокету клієнта
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Підключення до сервера за IP-адресою та портом
client_socket.connect(('127.0.0.1', 8080))

print("Підключено до сервера.")
print("Введіть 'exit' для завершення розмови.")

while True:
    # Введення повідомлення для відправки серверу
    message = input("Ви: ")

    # Надсилання повідомлення на сервер
    client_socket.send(message.encode())

    # Перевірка, чи клієнт не хоче завершити розмову
    if message.lower() == 'exit':
        break

    # Очікування отримання відповіді від сервера
    response = client_socket.recv(1024).decode()

    # Виведення отриманої відповіді
    print(f"Сервер : {response}")

# Повідомлення про завершення розмови
print("Розмову завершено.")

# Закриття з'єднання з сервером
client_socket.close()

# Чекаємо нового клієнта
print("Чекаємо нового учасника розмови...")
