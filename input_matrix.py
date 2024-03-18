import numpy as np


def input_matrix(rows, cols):
    matrix = []
    print("Enter the matrix elements row by row:")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("The number of elements in the row does not match the desired number of columns.")
            return None
        matrix.append(row)
    return np.array(matrix)
