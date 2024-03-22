def input_matrix(rows, cols):
    matrix = []
    print("Enter the matrix elements row by row:")
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print("The number of elements in the row does not match the desired number of columns.")
            return None
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print("|"," | ".join(map(str, row)),"|")

# Matrix Operations functions (+, -, *)
def increase_matrix(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix1[i][j] = matrix1[i][j] + matrix2[i][j]
    return matrix1

def decrease_matrix(matrix1, matrix2):
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix1[i][j] = matrix1[i][j] - matrix2[i][j]
    return matrix1

def matrix_scalar_multiplication(matrix, scalar):
    result = []
    for i in range(len(matrix)):
        row_result = []
        for j in range(len(matrix[0])):
            row_result.append(matrix[i][j] * scalar)
        result.append(row_result)
    return result

def matrix_multiplication(matrix1, matrix2):
    """Multiply two matrices."""
    if len(matrix1[0]) != len(matrix2):
        print("Number of columns in the first matrix is not equal to the number of rows in the second matrix.")
        return None

    result = []
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix2[0])):
            total = 0
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            row_result.append(total)
        result.append(row_result)
    return result

# Transpose a matrix function

def transpose_matrix(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create a new matrix to store the transposed matrix
    transposed_matrix = []
    for j in range(num_cols):
        new_row = []
        for i in range(num_rows):
            new_row.append(matrix[i][j])
        transposed_matrix.append(new_row)

    return transposed_matrix

# Determinant of a matrix function
def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def determinant_3x3(matrix):
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[0][2]
    d = matrix[1][0]
    e = matrix[1][1]
    f = matrix[1][2]
    g = matrix[2][0]
    h = matrix[2][1]
    i = matrix[2][2]
    
    return (a * (e*i - f*h)) - (b * (d*i - f*g)) + (c * (d*h - e*g))

def lu_decomposition(matrix):
    n = len(matrix)
    lower = [[0.0] * n for _ in range(n)]
    upper = [[0.0] * n for _ in range(n)]

    for i in range(n):
        lower[i][i] = 1.0

    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i):
                sum += (lower[i][k] * upper[k][j])
            upper[i][j] = matrix[i][j] - sum

        for j in range(i, n):
            if i == j:
                if upper[i][j] == 0:
                    raise ValueError("Singular matrix: Division by zero")
                lower[j][i] = 1.0
            else:
                if upper[i][i] == 0:
                    raise ValueError("Singular matrix: Division by zero")
                lower[j][i] = (matrix[j][i] - sum) / upper[i][i]

    det = 1
    for i in range(n):
        det *= upper[i][i]
    return det

def determinant_matrix(matrix):
    n = len(matrix)
    if n == 2:
        return determinant_2x2(matrix)
    elif n == 3:
        return determinant_3x3(matrix)
    else:
        return lu_decomposition(matrix)

# Invers matrix function
def inverse_matrix(matrix, decimal_places=2):
    n = len(matrix)
    identity = [[0] * n for _ in range(n)]
    for i in range(n):
        identity[i][i] = 1

    # Augment the matrix with the identity matrix
    augmented_matrix = [row + identity_row for row, identity_row in zip(matrix, identity)]

    # Perform row operations to reduce the left half to the identity matrix
    for i in range(n):
        pivot = augmented_matrix[i][i]
        if pivot == 0:
            raise ValueError("Matrix is singular, cannot find inverse")
        for j in range(n*2):
            augmented_matrix[i][j] /= pivot
        for k in range(n):
            if k != i:
                factor = augmented_matrix[k][i]
                for j in range(n*2):
                    augmented_matrix[k][j] -= factor * augmented_matrix[i][j]

    # Extract the right half (the inverse matrix)
    inverse_matrix = [row[n:] for row in augmented_matrix]

    # Round the elements to the specified number of decimal places
    rounded_inverse_matrix = [[round(elem, decimal_places) for elem in row] for row in inverse_matrix]

    return rounded_inverse_matrix