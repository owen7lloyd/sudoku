import numpy as np


def solve(board):
    board = np.asarray(board)
    current_board = np.copy(board)
    row, col, backtrack = 0, 0, True
    manual_entries = []
    while backtrack:
        val = current_board[row, col]
        if val == board[row, col] and val != 0:  # if the entry was predefined
            row, col = move(row, col, True)
        else:
            in_square = True
            new_val = val
            while in_square:
                new_val += 1
                if new_val == 10:
                    current_board[row, col] = 0
                    row, col = manual_entries.pop()
                    in_square = False
                else:
                    if check_board(current_board, row, col, new_val):
                        current_board[row, col] = new_val
                        manual_entries.append((row, col))
                        row, col = move(row, col, True)
                        in_square = False
        if row == 9:
            backtrack = False
    print(current_board)


def move(row, col, forward):
    if forward:
        if col == 8:
            new_row = row + 1
            new_col = 0
        else:
            new_col = col + 1
            new_row = row
    else:
        if col == 0:
            new_col = 8
            new_row = row - 1
        else:
            new_col = col - 1
            new_row = row

    return new_row, new_col


def check_board(board, row, col, val):
    in_row = val in board[row, :]
    in_col = val in board[:, col]
    in_square = (
        val
        in board[
            (row // 3) * 3 : (row // 3 + 1) * 3, (col // 3) * 3 : (col // 3 + 1) * 3
        ]
    )
    return not (in_row or in_col or in_square)


if __name__ == "__main__":
    board = [
        [0, 0, 0, 2, 6, 0, 7, 0, 1],
        [6, 8, 0, 0, 7, 0, 0, 9, 0],
        [1, 9, 0, 0, 0, 4, 5, 0, 0],
        [8, 2, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 4, 6, 0, 2, 9, 0, 0],
        [0, 5, 0, 0, 0, 3, 0, 2, 8],
        [0, 0, 9, 3, 0, 0, 0, 7, 4],
        [0, 4, 0, 0, 5, 0, 0, 3, 6],
        [7, 0, 3, 0, 1, 8, 0, 0, 0],
    ]
    solve(board)
