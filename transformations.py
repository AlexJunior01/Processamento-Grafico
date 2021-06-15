import numpy as np
from Object import Object


def cross_product(a, b):
    r1 = a[1]*b[2] - a[2]*b[1]
    r2 = a[2]*b[0] - a[0]*b[2]
    r3 = a[0]*b[1] - a[1]*b[0]

    return np.array([r1, r2, r3])


def get_vector_length(v):
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
    result = np.zeros(col)

    for i in range(col):
        aux = matrix[i][:] * [vector[0], vector[1], vector[2], vector[3]]
        result[i] = np.sum(aux)
    return result.tolist()


def world_to_view(matrix_view, object):
    new_vertices = []
    for k, vertex in enumerate(object.vertices):
        vert_aux = vertex.copy()
        vert_aux.append(1)
        new_vertex = matrix_vector_multiplication(matrix_view, vert_aux)
        new_vertices.append(new_vertex[:3])

    new_object = Object(new_vertices, object.faces)
    return new_object

def view_port(object, width, height):
    height = height/2
    width = width/2
    object.translate([1, 1, 0])
    object.scale([width, height, 0])

    return object