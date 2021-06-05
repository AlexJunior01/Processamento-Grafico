from Object import Object
import numpy as np

cube = Object("objects/coarseTri.cube.obj")
# obj = Object("objects/coarseTri.cube.obj")
# cube.translate([3, 0, 0])
# obj.translate(([3, 2, -3]))
# obj.scale((0.5, 0.5, 0.5))
# cube.save_file("my_cube.obj")
# obj.save_file("point.obj")


def cross_product(a, b):
    r1 = a[1]*b[2] - a[2]*b[1]
    r2 = a[2]*b[0] - a[0]*b[2]
    r3 = a[0]*b[1] - a[1]*b[0]

    return np.array([r1, r2, r3])


def get_vector_lenght(v):
    length = 0
    for i in range(len(v)):
        length += v[i]**2

    length = np.sqrt(length)
    return length


def matrix_multiplication(m, n):
    lin = m.shape[0]
    col = n.shape[1]
    result = np.zeros((lin, col))
    for i in range(lin):
        for j in range(col):
            aux = m[i][:] * [n[0][j], n[1][j], n[2][j], n[3][j]]
            result[i][j] = np.sum(aux)

    return result


def matrix_vector_multiplication(matrix, vector):
    col = matrix.shape[1]
    result = np.zeros((col, 1))

    for i in range(col):
        aux = matrix[i][:] * [vector[0], vector[1], vector[2], vector[3]]
        result[i] = np.sum(aux)
    return result


def create_camera(pos, look_at):
    view_up = pos + [0, 1, 0]
    T = np.identity(4)
    T[0][3] = -pos[0]
    T[1][3] = -pos[1]
    T[2][3] = -pos[2]

    n = look_at - pos
    n = n/get_vector_lenght(n)
    u = cross_product(view_up, n)
    u = u/get_vector_lenght(u)
    v = cross_product(n, u)

    R = np.identity(4)
    R[0][0:3] = u
    R[1][0:3] = v
    R[2][0:3] = n

    M = matrix_multiplication(R, T)
    return M


def model_to_view(M, vertices):
    new_vertices = []
    for k, vertex in enumerate(vertices):
        

