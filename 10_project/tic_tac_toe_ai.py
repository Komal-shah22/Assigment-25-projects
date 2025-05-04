import math

# Function to print the board
def print_board(board):
    """
    Prints the Tic-Tac-Toe board.
    """
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if there is a winner
def check_winner(board):
    """
    Checks if there is a winner.
    Returns 'X' or 'O' if a player wins, or None otherwise.
    """
    for i in range(3):
        # Check rows and columns
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None  # No winner

# Function to check if the board is full
def is_full(board):
    """
    Checks if the board is full (draw).
    """
    return all(cell != " " for row in board for cell in row)

# Function to get available moves
def get_available_moves(board):
    """
    Returns a list of available (empty) positions.
    """
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

# Minimax algorithm for AI
def minimax(board, is_maximizing):
    """
    Minimax algorithm to determine the best move for the AI.
    """
    winner = check_winner(board)
    if winner == "X":
        return -1  # Player win
    elif winner == "O":
        return 1  # AI win
    elif is_full(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for (r, c) in get_available_moves(board):
            board[r][c] = "O"
            score = minimax(board, False)
            board[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (r, c) in get_available_moves(board):
            board[r][c] = "X"
            score = minimax(board, True)
            board[r][c] = " "
            best_score = min(score, best_score)
        return best_score

# Function for AI move
def ai_move(board):
    """
    Determines the best move for the AI using the minimax algorithm.
    """
    best_score = -math.inf
    best_move = None

    for (r, c) in get_available_moves(board):
        board[r][c] = "O"
        score = minimax(board, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            best_move = (r, c)

    board[best_move[0]][best_move[1]] = "O"

# Function for player move
def player_move(board):
    """
    Allows the player to enter a move.
    """
    while True:
        try:
            move = int(input("\nEnter your move (1-9): ")) - 1
            row, col = divmod(move, 3)

            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print(" This position is already taken! Try again.")
        except (ValueError, IndexError):
            print(" Invalid input! Enter a number between 1 and 9.")

# Main function to play Tic-Tac-Toe
def tic_tac_toe():
    """
    Runs the Tic-Tac-Toe game with AI.
    """
    print("\n========= WELCOME TO TIC-TAC-TOE WITH AI! ========\n")
    
    board = [[" " for _ in range(3)] for _ in range(3)]

    print(" You are 'X', AI is 'O'. Try to beat the AI! \n")
    print_board(board)

    while True:
        # Player move
        player_move(board)
        print_board(board)

        if check_winner(board) == "X":
            print("\n\t\t\t========== Congratulations! You win! ==========\n")
            break
        if is_full(board):
            print("\n\t\t\t========== It's a Draw! ==========\n")
            break

        # AI move
        print("\n AI is thinking... ")
        ai_move(board)
        print_board(board)

        if check_winner(board) == "O":
            print("\n\t\t\t======== AI wins! Better luck next time! ========\n")
            break
        if is_full(board):
            print("\n\t\t\t======== It's a Draw! ========\n")
            break

# Start the game
tic_tac_toe()
