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

def cheo_hoa(matrix):
    cheo_hoa_matrix = np.array(matrix)
    eigen_values, eigen_vectors = np.linalg.eig(cheo_hoa_matrix)
    diagonal = np.diag(eigen_values)
    p = eigen_vectors
    min_vals = p.min(axis=0)
    for i in range(len(min_vals)):
        for j in range(len(min_vals)):
            p[j,i] //= min_vals[i]
    p_inversed = np.linalg.inv(p)
    return p, diagonal, p_inversed

