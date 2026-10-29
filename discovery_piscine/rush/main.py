#!/usr/bin/env python3
import random
import math as m

# Code
def show_menu():
    print(r""" 
   _____  __________ ______  _  __  ____      __   ___   ___  ___  _______ 
  / _ \ \/ /_  __/ // / __ \/ |/ / / __/___  / /  / _ | / _ \/ _ \/ __/ _ \
 / ___/\  / / / / _  / /_/ /    /  > _/_ _/ / /__/ __ |/ // / // / _// , _/
/_/    /_/ /_/ /_//_/\____/_/|_/  |_____/  /____/_/ |_/____/____/___/_/|_| 

1. Start
2. Rules
3. Exit  
    """)

BOARD_SIZE = 5
TOTAL_SQUARES = BOARD_SIZE * BOARD_SIZE
P1 = int(1)
P1_name = str()
P2 = int(1)
P2_name = str()
dice = int()

def players_position():
    if P1 == P2:
                print(f"Both players are currently at square {P1}.")
    else:
                print(f"{P1_name} is at square {P1}.") 
                print(f"{P2_name} is at square {P2}.")


def board_setup(): #format for the board
    board = []
    number = 1

    # Create a 5 x 5 board
    for row in range(BOARD_SIZE):
        current_row = []

        for col in range(BOARD_SIZE):
            current_row.append(number)
            number += 1

        # Reverse every other row for the usual
        # Snake and Ladder numbering pattern
        if row % 2 == 1:
            current_row.reverse()

        board.append(current_row)

    # Display the highest-numbered row at the top
    board.reverse()
    return board

def show_board(board): # for displaying the board
    print(r"◤━━━━━━━━━━━━━━━━◥")
    for row in board:
        for square in row:
            print(f"{square:2}", end="  ")
        print()
    print(r"◣━━━━━━━━━━━━━━━━◢")


def generate_ladder_and_snake():
    # Generate ladder
    ladder_start = random.randint(2, TOTAL_SQUARES - 6)
    ladder_end = random.randint(ladder_start + 5, TOTAL_SQUARES)

    # Generate snake
    snake_start = random.randint(6, TOTAL_SQUARES)
    snake_end = random.randint(1, snake_start - 5)

    # Regenerate if any positions overlap
    while (
        ladder_start in (snake_start, snake_end)
        or ladder_end in (snake_start, snake_end)
    ):
        ladder_start = random.randint(2, TOTAL_SQUARES - 6)
        ladder_end = random.randint(ladder_start + 5, TOTAL_SQUARES)

        snake_start = random.randint(6, TOTAL_SQUARES)
        snake_end = random.randint(1, snake_start - 5)

    return ladder_start, ladder_end, snake_start, snake_end


# Interface
def main():
    show_menu()
    while True:
        choice = input("(1-3): ")
        if choice == '1': 
            P1 = 1
            P2 = 1
            #Enter names
            P1_name = input("Player 1, enter your name: ")
            if P1_name == "":
                print("Name empty, defaulting to 'Player 1'.")
            P1_name = "Player 1"
            P2_name = input("Player 2, enter your name: ")
            if P2_name == "":
                print("Name empty, defaulting to 'Player 2'.")
            P2_name = "Player 2"

            #Setting up board
            board = board_setup()
            show_board(board)
            Ladder1_start, Ladder1_end, Snake1_start, Snake1_end = generate_ladder_and_snake()
            print(f"A ladder starts at square {Ladder1_start} and ends at square {Ladder1_end}.")
            print(f"A python starts at square {Snake1_start} and ends at square {Snake1_end}.")
            first_player = random.choice([P1_name, P2_name])
            print(f"{first_player} will start the game.")
            
            players_position()
            
            dice = input("Press Enter to roll the dice...")
            dice = random.randint(1, 6)
            print(f"{first_player} rolled a {dice}!")    

        elif choice == '2':
            print(r''' 
-= RULES =-
The game consists of 2 players. Each player takes turns to roll a dice (1-6) to move. 
The first player to reach the end of the board wins.
-= Gameplay Elements =-
The board (5x5) includes a ladder and a python placed at random square.
Ladder: climb up to a higher position on the board.
Python: slide down to a lower position on the board.
''')

        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__": #start the program
    main()
