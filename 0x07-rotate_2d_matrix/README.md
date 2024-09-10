# Rotate 2D Matrix

This project contains a Python function that rotates a given n x n 2D matrix 90 degrees clockwise. The rotation is performed in-place, meaning the original matrix is modified without creating a new matrix.

## Requirements

- Ubuntu 20.04 LTS
- Python 3.8.10
- pycodestyle 2.8.0

## File Description

- `0-rotate_2d_matrix.py`: Contains the implementation of the `rotate_2d_matrix` function.

## Function Prototype

```python
def rotate_2d_matrix(matrix):
```

## Usage

```python
#!/usr/bin/python3
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
```

## Example

Input:

```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]
```

Output:

```
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
```
