from utils import print_matrix, determinant_matrix


#3. How To Find The Determinant Matrix
def searchDeterminantMatrix(A, B):
    chooseMatrix = input("which matrix to search for looking determinant? (a/b): ")
    if chooseMatrix == 'a' or chooseMatrix == 'A':
        print("the matrix A: ")
        print_matrix(A)
        print('the determinant of matrix A is: ', determinant_matrix(A))
    elif chooseMatrix == 'b' or chooseMatrix == 'B':
        print("the matrix B: ")
        print_matrix(B)
        print('the determinant of matrix B is: ', determinant_matrix(B))

    
