import random

matrix_size = 128
matrix1 = [[random.randint(0,9) for i in range(matrix_size)] for j in range(matrix_size)]
matrix2 = [[random.randint(0,9) for i in range(matrix_size)] for j in range(matrix_size)]


def add(matrix1,matrix2):
    matrix3 = [[0 for i in range(matrix_size)] for j in range(matrix_size)]
    for i in range(matrix_size):
        for j in range(matrix_size):
            matrix3[i][j]= matrix1[i][j]+ matrix2[i][j]
    return matrix3


print(matrix1)
print(matrix2)
print(add(matrix1,matrix2))