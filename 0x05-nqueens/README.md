# N Queens Solver

## Description

This project contains a Python script that solves the N Queens puzzle. The N Queens puzzle is the challenge of placing N chess queens on an N×N chessboard so that no two queens threaten each other. Thus, a solution requires that no two queens share the same row, column, or diagonal.

## Requirements

- Python 3
- Ubuntu 20.04 LTS

## File

- `0-nqueens.py`: The main Python script that solves the N Queens problem.

## Usage

To run the N Queens solver, use the following command:

```
./0-nqueens.py N
```

Where `N` is an integer greater than or equal to 4, representing the size of the chessboard and the number of queens to place.

### Examples:

```
./0-nqueens.py 4
./0-nqueens.py 6
```

## Output

The program will print every possible solution to the N Queens problem. Each solution is represented as a list of queen positions, where each queen's position is denoted by [row, column].

Example output for N = 4:

```
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

## Error Handling

The script includes error handling for the following cases:

- If the user doesn't provide exactly one argument: "Usage: nqueens N"
- If the argument is not an integer: "N must be a number"
- If N is smaller than 4: "N must be at least 4"

In each of these cases, the program will print the corresponding error message and exit with a status code of 1.

## How It Works

The script uses a backtracking algorithm to find all possible solutions. It starts by placing a queen in the first column and then recursively tries to place queens in the subsequent columns. If a placement violates the rules, the algorithm backtracks and tries a different position.

## Note

This is a beginner-friendly implementation with descriptive variable and function names to aid understanding. Feel free to explore and modify the code to learn more about backtracking algorithms and the N Queens problem!
