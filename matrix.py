from operations import matrixOperation
from transpose import searchTransposeMatrix
from determinant import searchDeterminantMatrix
from inverse import searchInverseMatrix
from utils import input_matrix, print_matrix

A = []
B = []
isChoosing =  True

while len(A) == 0 and len(B) == 0:
    print('Please indetify the matrix A and B before calculating')
    rows = int(input("Enter the number of rows of the matrix: "))
    cols = int(input("Enter the number of columns of the matrix: "))

    # Input matriks A
    print("\nEnter matrix A:")
    A = input_matrix(rows, cols)
    print("matriks A is: ")
    print_matrix(A)

    # Input matriks B
    print("\nEnter matrix B:")
    B = input_matrix(rows, cols)
    print("matriks B is: ")
    print_matrix(B)

while isChoosing:
    print('================================')
    print('what are you looking for in the matrix?')
    print('1. Matrix Operation (+, -, x)')
    print('2. Transpose Matrix')
    print('3. Find The Determinant Matrix')
    print('4. Find The Inverse Matrix')
    print('5. Exit')
    print('================================')
    print('note: write the number above')
    typeMatrix = input("Type the matrix: ")
    if typeMatrix == '1':
        #1. Matrix Operation (+, -, x)
        matrixOperation(A, B)
    elif typeMatrix == '2':
        #2. How to Transpose Matrix
        searchTransposeMatrix(A, B)
    elif typeMatrix == '3':
        #3. How To Find The Determinant Matrix
        searchDeterminantMatrix(A,B)
    elif typeMatrix == '4':
        #4. How To Find The Inverse Matrix
        searchInverseMatrix(A, B)
    elif typeMatrix == '5':
        isChoosing = False
        break

    print('--------------------------------')
    nextAction = input('Do you want to calculate matrix again? (y/n): ')
    if nextAction == 'y' or nextAction == 'Y':
        isChoosing = True
    elif nextAction == 'n' or nextAction == 'N':
        isChoosing = False
        print('Thank you for using this program.')




