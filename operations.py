from input_matrix import input_matrix
import numpy as np



#1. Matrix Operation (+, -, x)
def matrixOperation ():
    rows = int(input("Enter the number of rows of the matrix: "))
    cols = int(input("Enter the number of columns of the matrix: "))

    # Input matriks A
    print("\nEnter matrix A:")
    A = input_matrix(rows, cols)
    if A is None:
        return
    print("matriks A is: ")
    print(A)

    # Input matriks B
    print("\nEnter matrix B:")
    B = input_matrix(rows, cols)
    if B is None:
        return
    print("matriks B is: ")
    print(B)

    print('Matriks A is: ')
    print(A)
    print('Matriks B is: ')
    print(B)
    print("Type of matrix operations:")
    print('1. Increase matrix ( + )')
    print('2. Decrease matrix ( - )')
    print('3. Multiply matrix ( * )')

    typeOperation = input("Choose the type of operation: ")

    if typeOperation == 'increase' or typeOperation == '+' or typeOperation == '1':
        print('You has Choose the type of operation ( increase ( + ) ) the result is:')
        print(A + B)
    elif typeOperation == 'decrease' or typeOperation == '-' or typeOperation == '2':
        print('You has Choose the type of operation ( decrease ( - ) ) the result is:')
        print(A - B)
    elif typeOperation == 'multiply' or typeOperation == '*' or typeOperation == '3':
        print('1.A * B')
        print('2.A * Skalar')
        print('3.B * Skalar')
        typeOperationMultiply = input('Choose the type of operation ( multiply): ')
        if typeOperationMultiply == '1':
            print('A * B is: ')
            print(np.dot(A, B))
        elif typeOperationMultiply == '2':
            skalar = int(input('Type Number Of Skalar:'))
            print('A * ', skalar, ' is: ')
            print(A * skalar)
        elif typeOperationMultiply == '3':
            skalar = int(input('Type Number Of Skalar: '))
            print('B * ', skalar,'is: ')
            print(B * skalar)

        print('You has Choose the type of operation ( Multiply ( * ) ) the result is:')
        print()
