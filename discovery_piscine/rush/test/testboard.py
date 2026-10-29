# Snake and Ladder: 25-Square Board

BOARD_SIZE = 5
TOTAL_SQUARES = BOARD_SIZE * BOARD_SIZE

def create_board():
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


def display_board(board):
    for row in board:
        for square in row:
            print(f"{square:2}", end="  ")
        print()


# Create and display the empty board
game_board = create_board()
display_board(game_board)