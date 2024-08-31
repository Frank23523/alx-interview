#!/usr/bin/python3
"""N Queens Solver"""
import sys


def print_solution(board):
    """Prints a board"""
    solution = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def is_queen_safe(board, row, col, board_size):
    """Check if a queen can be placed on board"""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, board_size, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, board_size):
    """Recursively attempt to place queens on the board"""
    # Base case: If all queens are placed, return True
    if col >= board_size:
        print_solution(board)
        return True

    for i in range(board_size):
        if is_queen_safe(board, i, col, board_size):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, board_size)
            board[i][col] = 0

    return False


def solve_n_queens(board_size):
    """Solve N queens"""
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]
    solve_n_queens_util(board, 0, board_size)


def main():
    """Execute"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Try to convert the argument to an integer
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if the board size is at least 4
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solve_n_queens(board_size)


if __name__ == "__main__":
    main()
