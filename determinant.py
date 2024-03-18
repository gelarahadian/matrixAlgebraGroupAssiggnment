from input_matrix import input_matrix
import numpy as np


#3. How To Find The Determinant Matrix
def searchDeterminantMatrix():
    rows = int(input("Enter the number of rows of the matrix: "))
    cols = int(input("Enter the number of columns of the matrix: "))
    # Input matriks A
    print("\nEnter matrix A:")
    A = input_matrix(rows, cols)
    if A is None:
        return
    
    print("Transpose of the matrix: ")
    print(A,  'is: ')
    print('----------------------------------------------------------------')
    print(np.linalg.det(A))
    
