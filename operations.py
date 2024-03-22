from utils import  print_matrix, increase_matrix, decrease_matrix, matrix_multiplication, matrix_scalar_multiplication


#1. Matrix Operation (+, -, x)
def matrixOperation (A, B):
    print('Matriks A is: ')
    print_matrix(A)
    print('Matriks B is: ')
    print_matrix(B)
    print("Type of matrix operations:")
    print('1. Increase matrix ( + )')
    print('2. Decrease matrix ( - )')
    print('3. Multiply matrix ( * )')

    typeOperation = input("Choose the type of operation: ")

    if typeOperation == 'increase' or typeOperation == '+' or typeOperation == '1':
        print('You has Choose the type of operation ( increase ( + ) ) the result is:')
        result = increase_matrix(A, B)
        print_matrix(result)
    elif typeOperation == 'decrease' or typeOperation == '-' or typeOperation == '2':
        print('You has Choose the type of operation ( decrease ( - ) ) the result is:')
        result = decrease_matrix(A, B)
        print_matrix(result)
    elif typeOperation == 'multiply' or typeOperation == '*' or typeOperation == '3':
        print('1.A * B')
        print('2.A * Skalar')
        print('3.B * Skalar')
        typeOperationMultiply = input('Choose the type of operation ( multiply): ')
        if typeOperationMultiply == '1':
            print('A * B is: ')
            result = matrix_multiplication(A, B)
            print_matrix(result)
        elif typeOperationMultiply == '2':
            skalar = int(input('Type Number Of Skalar:'))
            result = matrix_scalar_multiplication(A, skalar)
            print('A * ', skalar, ' is: ')
            print_matrix(result)
        elif typeOperationMultiply == '3':
            skalar = int(input('Type Number Of Skalar: '))
            result = (matrix_scalar_multiplication(B, skalar))
            print('B * ', skalar,'is: ')
            print_matrix(result)
    
