import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_board()
        self.assign_values_to_board()
        self.dug = set()  # track dug locations

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size ** 2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1

        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):
        num_bombs = 0
        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    num_bombs += 1
        return num_bombs

    def dig(self, row, col):
        self.dug.add((row, col))

        if self.board[row][col] == '*':
            return False
        elif self.board[row][col] > 0:
            return True

        for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
            for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)

        return True

    def __str__(self):
        visible_board = [[' ' for _ in range(self.dim_size)] for _ in range(self.dim_size)]
        for row, col in self.dug:
            visible_board[row][col] = str(self.board[row][col])
        string_rep = ''
        widths = [max(len(str(visible_board[i][j])) for i in range(self.dim_size)) for j in range(self.dim_size)]
        indices_row = '   ' + '  '.join(f'{i}'.rjust(widths[i]) for i in range(self.dim_size)) + '\n'
        string_rep += indices_row

        for i in range(self.dim_size):
            row_str = f'{i} '
            for j in range(self.dim_size):
                val = visible_board[i][j]
                row_str += f' {val}'.rjust(widths[j] + 1)
            string_rep += row_str + '\n'
        return string_rep

def play(dim_size=10, num_bombs=10):
    print("\n~~~~~~~~~~ WELCOME TO MINESWEEPER! ~~~~~~~~~~")
    print("Uncover all safe tiles without stepping on a bomb!\n")
    
    board = Board(dim_size, num_bombs)
    safe = True

    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = input("Enter location to dig (row,col): ")
        match = re.match(r"^(\d+),\s*(\d+)$", user_input)
        if not match:
            print("Invalid input. Try again.\n")
            continue

        row, col = int(match.group(1)), int(match.group(2))

        if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
            print("Out of bounds. Try again.\n")
            continue

        safe = board.dig(row, col)
        if not safe:
            break

    if safe:
        print("\n🎉 Congratulations! You won!")
    else:
        print("\n💣 Oops! You hit a bomb! Game Over.")
        board.dug = {(r, c) for r in range(dim_size) for c in range(dim_size)}
        print(board)

# Main loop to allow replay
while True:
    play()
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay != 'yes':
        print("\nThanks for playing Minesweeper! 👋")
        break
3