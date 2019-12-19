import socket
import numpy as np
import sys
import math
import pickle

        

"""skapar variabler för rader & kolumnerna som skapas i boarden,
blir lättare ifall man vill ändra storlek på boarden"""
ROW_COUNT = 6
COLUMN_COUNT = 7

    #skapar spelbrädet
def game_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def for_test_only():
    return True

#funktion som skapar "spelbrickan"
def drop_disc(board, row, col, disc):
    board[row][col] = disc
#kollar så att det inte redan ligger något där man vill placera spelbrickan
def is_drop_valid(board,col):
    return board[ROW_COUNT-1][col] == 0
#kollar vilken nästa postion för placering blir så inte man kan placera på samma plats
def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col-1] == 0:
            return r

#vänder på spelbrädet så att inmatningar börjar längst ner
def print_board(board):
    print(np.flip(board,0))

#kollar vinster horisontellt/vertikalt och diagonalt.
def winning_rows(board,disc):
    # kollar 4 i rad horisontellt
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == disc and board[r][c+1] == disc and board[r][c+2] == disc and board[r][c+3] == disc:
                return True
    # kollar 4 i rad vertikalt
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == disc and board[r+1][c] == disc and board[r+2][c] == disc and board[r+3][c] == disc:
                return True
    # kollar 4 i rad om diagonalen lutar uppåt 
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == disc and board[r+1][c+1] == disc and board[r+2][c+2] == disc and board[r+3][c+3] == disc:
                return True
    # kollar 4 i rad om diagonalen lutar neråt
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == disc and board[r-1][c+1] == disc and board[r-2][c+2] == disc and board[r-3][c+3] == disc:
                return True

board = game_board() 

def receive_and_send():
    
    turn = 0

    while True:
        data = pickle.loads(conn.recv(2048))
        col = data

        if turn == 0:
                       
            if is_drop_valid(board,col):
                row = get_next_open_row(board,col)
                drop_disc(board, row, col-1, 1)
                
                if winning_rows(board, 1):
                    print("Player 1 wins !")
                    print(np.flip(board,0))
                    winner_1 = pickle.dumps("Player 1 wins !")
                    conn.send(winner_1)
                    conn.close()
                    break
        
        if turn == 1:
            
            if is_drop_valid(board,col):
                row = get_next_open_row(board,col)
                drop_disc(board, row, col-1, 2)
                
                if winning_rows(board, 2):
                    print("player 2 wins !!")
                    print(np.flip(board,0))
                    winner_2 = pickle.dumps("Player 2 wins !!")
                    conn.send(winner_2)
                    conn.send(game_board)
                    conn.close()
                    break
                        
        print(np.flip(board,0))
        game_board = pickle.dumps(np.flip(board,0))
        conn.send(game_board)
        
        turn = (turn + 1)% 2      
        

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Waiting for connection...")

    host = "127.0.0.1"
    port = 65432
    s.bind((host, port))
    s.listen(2)
    conn, addr = s.accept()

    print("Connected by:" , addr)      
    receive_and_send()
                            
                                    
        















          

