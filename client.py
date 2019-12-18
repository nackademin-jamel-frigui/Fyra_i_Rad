import socket
import numpy as np
import pickle
import sys


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 65432
addr = (host, port)
client.connect(addr)


def send_and_receive():
    
    turn = 0

    while True:    
        if turn == 0:
            data = pickle.dumps(int(input("Player 1 Make your selection (1-7):")))
            client.send(data)
            data = pickle.loads(client.recv(4096))
            if data == "Player 1 wins !":
                print(data)
                break
        
        if turn == 1:
            data = pickle.dumps(int(input("Player 2 Make your selection (1-7):")))
            client.send(data)
            data = pickle.loads(client.recv(4096))
            if data == "Player 2 wins !!":
                print(data)
                break

        turn = (turn + 1) % 2                
        print(data)
        
send_and_receive()

    










