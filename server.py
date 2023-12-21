import socket
import threading
#створення сокету
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
#чекаємо підключення клієнта
server_socket.listen(5)
print("Чекаємо з'єднанння...")
#функція для обробки запитів клієнта
def handle_client(client_socket, address):
    print(f"Підключення з {address} було створене!")
    while True:
        location = client_socket.recv(1024).decode()
        if not location:
            break
        with open("weather_data.txt", 'r') as file:
            data = file.readlines()
            for loc in data:
                if location in loc:
                    response = loc
        client_socket.send(response.encode())
    print("Клієнт відвалився")
    client_socket.close()

while True:
    client_socket, address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()