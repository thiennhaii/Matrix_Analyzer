import numpy as np

def transpose_matrix(matrix):
    return matrix.transpose()

def determinant(matrix):
    np_matrix = np.array(matrix)
    if np_matrix.shape[0] == np_matrix.shape[1]:
        return np.linalg.det(matrix)
    else:
        return "Khong la ma tran vuong"