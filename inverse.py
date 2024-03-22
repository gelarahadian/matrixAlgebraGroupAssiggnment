from utils import print_matrix, inverse_matrix, determinant_matrix

#4. How To Find The Inverse Matrix
def searchInverseMatrix(A,B):
    chooseMatrix = input("which matrix to search for looking determinant? (a/b): ")
    if chooseMatrix == 'a' or chooseMatrix == 'A':
        det_A = determinant_matrix(A)
        if det_A != 0:
            A_inv = inverse_matrix(A)
            print("The inverse matrix of the matrix ")
            print_matrix(A)
            print('is: ')
            print('----------------------------------------------------------------')
            print_matrix(A_inv)
        else:
            print('The determinant of the matrix is 0, so the inverse matrix is not possible.')
    elif chooseMatrix == 'b' or chooseMatrix == 'B':
        det_B = determinant_matrix(B)
        if det_B != 0:
            B_inv = inverse_matrix(B)
            print("The inverse matrix of the matrix ")
            print_matrix(A)
            print('is: ')
            print('----------------------------------------------------------------')
            print_matrix(A_inv)
        else:
            print('The determinant of the matrix is 0, so the inverse matrix is not possible.')

