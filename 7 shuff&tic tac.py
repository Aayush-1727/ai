1. shufle deck cards:

import random


suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
         'Jack', 'Queen', 'King', 'Ace']


deck = [rank + ' of ' + suit for suit in suits for rank in ranks]

random.shuffle(deck)

print("Shuffled deck of cards:")
for card in deck:
    print(card)

2 tic tac toe

board = [" " for i in range(9)]

def display():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check_winner(player):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] == player:
            return True

    return False

player = "X"

for turn in range(9):
    display()

    position = int(input("Player " + player + ", enter position (1-9): ")) - 1

    if board[position] != " ":
        print("Position already occupied!")
        continue

    board[position] = player

    if check_winner(player):
        display()
        print("Player", player, "wins!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"
else:
    display()
    print("It's a draw!")