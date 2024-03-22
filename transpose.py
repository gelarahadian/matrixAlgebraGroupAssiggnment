from utils import print_matrix, transpose_matrix

#2. How to Transpose Matrix
def searchTransposeMatrix(A, B):    
    chooseMatrix = input("which matrix to search for transpose? (a/b): ")
    if chooseMatrix == 'a' or chooseMatrix == 'A':
        print_matrix(A)
        print('the transpose of matrix A is: ')
        print('--------------------------------')
        print_matrix(transpose_matrix(A))
    elif chooseMatrix == 'b' or chooseMatrix == 'B':
        print_matrix(B)
        print('the transpose of matrix B is: ')
        print('--------------------------------')
        print_matrix(transpose_matrix(B))
