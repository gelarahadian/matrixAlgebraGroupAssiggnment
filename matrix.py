from operations import matrixOperation
from transpose import searchTransposeMatrix
from determinant import searchDeterminantMatrix
from inverse import searchInverseMatrix


def main():
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
        matrixOperation()
    elif typeMatrix == '2':
        #2. How to Transpose Matrix
        searchTransposeMatrix()
    elif typeMatrix == '3':
        #3. How To Find The Determinant Matrix
        searchDeterminantMatrix()
    elif typeMatrix == '4':
        #4. How To Find The Inverse Matrix
        searchInverseMatrix()
    elif typeMatrix == '5':
        exit()

main()



