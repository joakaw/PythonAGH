import random
import numpy


def matrix_det(matrix):
    matrix = numpy.array(matrix)
    matrix_size = get_matrix_size(matrix)
    if matrix_size == 2:
        return min_matrix_det(matrix)
    else:
        det = 0
        for i in range(matrix_size):
            det = det + (pow(-1, i+2)*matrix[i][0]*matrix_det(get_min_matrix(matrix, i+1)))
        return det


def min_matrix_det(matrix):
    d = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return d


def get_min_matrix(matrix, i):
    matrix = numpy.array(matrix)
    matrix_size = get_matrix_size(matrix)
    if i == 1:
        return matrix[1:, 1:]
    elif i == matrix_size:
        return matrix[0:matrix_size-1, 1:]
    else:
        det1 = matrix[0:i-1,1:]
        det2 = matrix[i:,1:]
        det = numpy.append(det1, det2, axis=0)
        return det


def get_matrix_size(matrix):
    matrix = numpy.array(matrix)
    return matrix.shape.__getitem__(0)


w = 3
rand_matrix = [[random.randint(0,9) for i in range(w)] for j in range(w)]
print("Matrix: \n",numpy.array(rand_matrix))
print("Matrix det: ", matrix_det(rand_matrix))



