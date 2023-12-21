
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))

print("Підключено до сервера.")

while True:
    text_to_translate = input("Введіть текст для перекладу (або натисніть Enter для виходу): ")
    if not text_to_translate:
        break

    client_socket.send(text_to_translate.encode())
    translated_text = client_socket.recv(1024).decode()

    print(f"Перекладений текст: {translated_text}")

print("Розмова завершена.")
client_socket.close()

