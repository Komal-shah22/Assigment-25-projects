import random

def print_board(board):
    """
    This function prints the Tic-Tac-Toe board.
    """
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """
    This function checks if a player has won the game.
    """
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    """
    This function checks if the board is full (Game Draw).
    """
    return all(cell != " " for row in board for cell in row)

def player_move(board, player):
    """
    This function takes input from the player and updates the board.
    """
    while True:
        try:
            move = int(input(f"\n{player}, enter a number (1-9): ")) - 1
            row, col = divmod(move, 3)  # Convert number to row and column

            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print(" This position is already taken! Try again.")
        except (ValueError, IndexError):
            print(" Invalid input! Enter a number between 1 and 9.")

def tic_tac_toe():
    """
    This is the main function that runs the game.
    """
    print("\n\t\t\t~~~~~~~~~ WELCOME TO TIC-TAC-TOE! ~~~~~~~~~\n")
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = random.choice(players)  # Randomly select the first player

    print_board(board)

    while True:
        print(f"\n {current_player}'s turn!")
        player_move(board, current_player)
        print_board(board)

        if check_winner(board, current_player):
            print(f"\n========= Congratulations! {current_player} wins! =========\n")
            break
        elif is_full(board):
            print("\n========= It's a Draw! No one wins! =========\n")
            break

        # Switch player
        current_player = "X" if current_player == "O" else "O"

# Start the game
tic_tac_toe()
