import socket

# створення сокету
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
# чекаємо підключення клієнта
server_socket.listen(1)
print("Чекаємо з'єднання...")
while True:
    client_socket, address = server_socket.accept()
    print(f"Підключення з {address} було створене!")

    # обмін повідомлення
    while True:
        # очікуємо повідомлення від клієнта
        massage = client_socket.recv(1024).decode()
        if massage.lower() == 'exit':
            break
        print("Client: ", massage)
        response = input("Server: ")
        client_socket.send(response.encode())

    # Повідомлення завершення розмови
    print("Розмову завершено")

    # закриваємо з'єднання з клієнтом'
    client_socket.close()
