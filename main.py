import random

num = 0
board = {num:'_' for num in range(1, 10)}

def printBoard():
    global board
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}")


printBoard()
