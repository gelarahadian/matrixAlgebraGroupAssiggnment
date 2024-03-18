from input_matrix import input_matrix
import numpy as np


#4. How To Find The Inverse Matrix
def searchInverseMatrix():
    rows = int(input("Enter the number of rows of the matrix: "))
    cols = int(input("Enter the number of columns of the matrix: "))
    # Input matriks A
    print("\nEnter matrix A:")
    A = input_matrix(rows, cols)
    if A is None:
        return
    
    det_A = np.linalg.det(A)
    if det_A != 0:
        A_inv = np.linalg.inv(A)
        print("The inverse matrix of the matrix ")
        print(A, 'is: ')
        print('----------------------------------------------------------------')
        print(A_inv)
    else:
        print('The determinant of the matrix is 0, so the inverse matrix is not possible.')
