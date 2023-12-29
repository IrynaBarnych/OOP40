import socket
import threading
from googletrans import Translator

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8081))
server_socket.listen(5)
print("Очікуємо підключення...")

translator = Translator()

def handle_client(client_socket, address):
    print(f"Підключення від {address} встановлено!")
    while True:
        # Receive target language and text from the client
        data = client_socket.recv(1024).decode()
        if not data:
            break

        target_language, text_to_translate = data.split('|')
        translated_text = translator.translate(text_to_translate, dest=target_language).text
        client_socket.send(translated_text.encode())
    print("Клієнт відключився")
    client_socket.close()

while True:
    client_socket, address = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
