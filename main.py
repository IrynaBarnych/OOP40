# server.py
import socket
import threading

def initialize_board():
    return [str(i) for i in range(1, 10)]

def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[i * 3], "|", board[i * 3 + 1], "|", board[i * 3 + 2], "|")

def check_win(board, player):
    win_coord = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]] == player:
            return True
    return False

def handle_client(client_socket, address):
    print(f"Connection from {address} established!")
    player_letters = {'player_1': 'X', 'player_2': 'O'}
    board = initialize_board()
    counter = 0

    while True:
        draw_board(board)
        player_token = player_letters['player_1'] if counter % 2 == 0 else player_letters['player_2']

        if player_token == 'X':
            player_answer = player_game(player_token, board, client_socket)
            board[player_answer - 1] = player_token
            if check_win(board, player_letters['player_1']):
                draw_board(board)
                client_socket.send("win".encode())
                break
        else:
            player_answer = player_game(player_token, board, client_socket)
            board[player_answer - 1] = player_token
            if check_win(board, player_letters['player_2']):
                draw_board(board)
                client_socket.send("win".encode())
                break

        counter += 1
        if counter == 9:
            draw_board(board)
            client_socket.send("draw".encode())
            break

    print(f"Game over for {address}")
    client_socket.close()

def player_game(player, board, client_socket):
    while True:
        client_socket.send("Your move.".encode())
        player_answer = int(client_socket.recv(1024).decode())
        if 1 <= player_answer <= 9 and board[player_answer - 1] == str(player_answer):
            return player_answer
        else:
            client_socket.send("Invalid move. Try again.".encode())

if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 8081))
    server_socket.listen(5)
    print("Waiting for connections...")

    while True:
        client_socket, address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()
