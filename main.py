"""
TicTacToe.py: druhý projekt do Engeto Online Python Akademie
author: Igor Polinskyi
email: igor.polinskyi@gmail.com
discord: Igor P.#5305
"""
from visual import logo, rules
import os

board_spots = {1: "1", 2: "2", 3: "3",
               4: "4", 5: "5", 6: "6",
               7: "7", 8: "8", 9: "9"}

turn = 0
prev_turn = -1
winner = None
play_game = True



# Game board
def printBoard(board_spots):
    print(board_spots[1] + " | " + board_spots[2] + " | " + board_spots[3])
    print("---------")
    print(board_spots[4] + " | " + board_spots[5] + " | " + board_spots[6])
    print("---------")
    print(board_spots[7] + " | " + board_spots[8] + " | " + board_spots[9])


def check_turn(turn):
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


def check_horizontal(board_spots):
    global winner
    # Horizontal
    if board_spots[1] == board_spots[2] == board_spots[3]:
        winner = board_spots[1]
        return True
    elif board_spots[4] == board_spots[5] == board_spots[6]:
        winner = board_spots[4]
        return True
    elif board_spots[7] == board_spots[8] == board_spots[9]:
        winner = board_spots[7]
        return True
    else:
        return False


def check_vertical(board_spots):
    global winner
    # Vertical
    if board_spots[1] == board_spots[4] == board_spots[7]:
        winner = board_spots[1]
        return True
    elif board_spots[2] == board_spots[5] == board_spots[8]:
        winner = board_spots[2]
        return True
    elif board_spots[3] == board_spots[6] == board_spots[9]:
        winner = board_spots[3]
        return True
    else:
        return False


def check_diagonal(board_spots):
    global winner
    # Diagonal
    if board_spots[1] == board_spots[5] == board_spots[9]:
        winner = board_spots[1]
        return True
    elif board_spots[3] == board_spots[5] == board_spots[7]:
        winner = board_spots[3]
        return True
    else:
        return False


def check_win():
    global play_game
    if check_horizontal(board_spots) or check_vertical(board_spots) or check_diagonal(board_spots):
        play_game = False
        os.system("cls" if os.name == "nt" else "clear")
        printBoard(board_spots)
        print(f"\n!!!The winner is '{winner}'!!!")


def check_draw():
    global play_game
    if turn > 8 and not check_win():
        play_game = False
        os.system("cls" if os.name == "nt" else "clear")
        printBoard(board_spots)
        print("\nThis is DRAW")


print(logo)


while play_game:
    os.system("cls" if os.name == "nt" else "clear")
    print(rules)
    printBoard(board_spots)

    if prev_turn == turn:
        print("Invalid spot selected, please try another one")
    prev_turn = turn
    print(
        f"Player's {str((turn % 2) + 1)} turn.\nPick your spot to place mark (or stone) or press 'q' to quit the game.")
    # Input from player
    choice = input()
    if choice == "q":
        play_game = False
    # Check correct input from user
    elif str.isdigit(choice) and int(choice) in board_spots:
        # Check if spot is available or is already occupied
        if not board_spots[int(choice)] in {"X", "O"}:
            # Place "X" or "O" on board spot according to users choice
            turn += 1
            board_spots[int(choice)] = check_turn(turn)
    # Check for win or draw
    check_win()
    check_draw()
