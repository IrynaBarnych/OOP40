# client.py
import socket

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8091))

    print("Підключено до сервера.")

    while True:
        game_status = client_socket.recv(1024).decode()
        if game_status == "win":
            print("Ви виграли!")
            break
        elif game_status == "draw":
            print("Гра закінчилася внічию!")
            break

        print(client_socket.recv(1024).decode())  # Відображення поточного стану дошки
        move = input("Введіть ваш хід (1-9): ")
        client_socket.send(str(move).encode())

    print("Гра завершена.")
    client_socket.close()

if __name__ == "__main__":
    main()
