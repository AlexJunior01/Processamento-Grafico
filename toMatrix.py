import numpy as np
from rasterizacao import *
from Vertex import Vertex
from PIL import Image


def save_image(shape, matrix, i):

    img = Image.new('1', shape)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = int(matrix[i][j])

    img.save(f't{i}.bmp')


def get_coordinates(ind_vertex, object):
    coordinates = []
    vertice = object.vertices[ind_vertex]

    for axis in vertice:
        coordinates.append(int(axis))

    return coordinates


def obj_to_matrix (x, y, object):
    matrix = np.zeros((x, y))
    
    for i, f in enumerate(object.faces):
        v1 = get_coordinates(f[0], object)
        v2 = get_coordinates(f[1], object)
        v3 = get_coordinates(f[2], object)

        vertex1 = Vertex(v1[0], v1[1])
        vertex2 = Vertex(v2[0], v2[1])
        vertex3 = Vertex(v3[0], v3[1])

        fill_triangle(matrix, vertex1, vertex2, vertex3)
    return matrix
