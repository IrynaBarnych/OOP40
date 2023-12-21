import socket
import threading
from googletrans import Translator

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8080))
server_socket.listen(5)
print("Очікуємо підключення...")

translator = Translator()

def handle_client(client_socket, address):
    print(f"Підключення від {address} встановлено!")
    while True:
        text_to_translate = client_socket.recv(1024).decode()
        if not text_to_translate:
            break
        translated_text = translator.translate(text_to_translate, dest='en').text
        client_socket.send(translated_text.encode())
    print("Клієнт відключився")
    client_socket.close()

while True:
    client_socket, address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()