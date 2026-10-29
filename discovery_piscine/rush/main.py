#!/usr/bin/env python3
import random

BOARD_SIZE = 5
TOTAL_SQUARES = BOARD_SIZE * BOARD_SIZE


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


def show_rules():
    print("""
-= RULES =-
The game has two players. Each player takes turns rolling a D6 (1-6).
The first player to reach square 25 wins.
You must roll the exact number to land on square 25.
The 5x5 board contains one ladder and one snake.
Ladder: landing on its start square moves you up to its end square.
Snake: landing on its start square moves you down to its end square.
""")
    input("Press Enter to return to the menu...")


def board_setup():
    board = []
    number = 1

    for row in range(BOARD_SIZE):
        current_row = []

        for col in range(BOARD_SIZE):
            current_row.append(number)
            number += 1

        # Reverse every other row to create the zigzag numbering pattern.
        if row % 2 == 1:
            current_row.reverse()

        board.append(current_row)

    # Show the highest-numbered row at the top.
    board.reverse()
    return board


def show_board(board):
    print("◤━━━━━━━━━━━━━━━━◥")
    for row in board:
        print("  ".join(f"{square:2}" for square in row))
    print("◣━━━━━━━━━━━━━━━━◢")


def players_position(players):
    print("\nCurrent positions:")
    for player in players:
        print(f"{player['name']}: square {player['position']}")


def generate_ladder_and_snake():
    # Keep generating until the ladder and snake use four different squares.
    while True:
        ladder_start = random.randint(2, TOTAL_SQUARES - 6)
        ladder_end = random.randint(ladder_start + 5, TOTAL_SQUARES)

        snake_start = random.randint(6, TOTAL_SQUARES)
        snake_end = random.randint(1, snake_start - 5)

        positions = [ladder_start, ladder_end, snake_start, snake_end]
        if len(set(positions)) == len(positions):
            return ladder_start, ladder_end, snake_start, snake_end


def play_game():
    # Ask for player names, using defaults only when the input is blank.
    p1_name = input("Player 1, enter your name: ").strip()
    if not p1_name:
        p1_name = "Player 1"

    p2_name = input("Player 2, enter your name: ").strip()
    if not p2_name:
        p2_name = "Player 2"

    # Keep each player's name and position together.
    # A list of dictionaries also allows both players to share the same name.
    players = [
        {"name": p1_name, "position": 1},
        {"name": p2_name, "position": 1},
    ]

    board = board_setup()
    show_board(board)

    ladder_start, ladder_end, snake_start, snake_end = generate_ladder_and_snake()
    print(f"\nLadder: square {ladder_start} -> square {ladder_end}")
    print(f"Snake:  square {snake_start} -> square {snake_end}")

    current_player = random.randint(0, 1)
    print(f"\n{players[current_player]['name']} will start the game.")

    while True:
        player = players[current_player]
        players_position(players)

        input(f"\n{player['name']}, press Enter to roll the dice...")
        dice = random.randint(1, 6)
        print(f"{player['name']} rolled a {dice}.")

        new_position = player["position"] + dice
        player["position"] = min(new_position, TOTAL_SQUARES)

        if player["position"] == ladder_start:
                print(f"Ladder! {player['name']} climbs to square {ladder_end}.")
                player["position"] = ladder_end
        elif player["position"] == snake_start:
                print(f"Snake! {player['name']} slides down to square {snake_end}.")
                player["position"] = snake_end

        if player["position"] == TOTAL_SQUARES:
            players_position(players)
            print(f"\n{player['name']} wins!")
            break

        # Switch to the other player.
        current_player = 1 - current_player


def main():
    show_menu()

    while True:
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            play_game()
            show_menu()
        elif choice == "2":
            show_rules()
            show_menu()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
