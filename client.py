# client.py
import socket

def отримати_файл(client_socket, ім_файлу):
    with open(ім_файлу, 'wb') as файл:
        дані = client_socket.recv(1024)
        while дані:
            файл.write(дані)
            дані = client_socket.recv(1024)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8093))

    ім_файлу = input("Введіть ім'я файлу для відправлення: ")
    client_socket.send(ім_файлу.encode())

    відповідь = client_socket.recv(1024).decode()
    print(відповідь)

    if відповідь.lower() == "готово":
        отримати_файл(client_socket, ім_файлу)
        print(f"Файл успішно отримано: {ім_файлу}")
    else:
        print("Відмовлено у передачі файлу.")

    client_socket.close()

if __name__ == "__main__":
    main()
