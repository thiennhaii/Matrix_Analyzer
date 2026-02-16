import numpy as np

def transpose_matrix(matrix):
    return matrix.transpose()

def determinant(matrix):
    np_matrix = np.array(matrix)
    if np_matrix.shape[0] == np_matrix.shape[1]:
        return np.linalg.det(matrix)
    else:
        return "Khong la ma tran vuong"

def rank(matrix):
    return np.linalg.matrix_rank(matrix)

def inverse(matrix):
    det = determinant(matrix)
    if type(det) != str:
        if det != 0:
            result = np.linalg.inv(matrix)
            return result
        else:
            return "Khong kha nghich"
    else:
        return "Khong la ma tran vuong"

def qr_factorization(matrix):
    qr_matrix = np.array(matrix)
    q,r = np.linalg.qr(qr_matrix)
    return (q, r)