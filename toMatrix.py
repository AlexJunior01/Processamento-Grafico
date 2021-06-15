import numpy as np
from StandarAlgorithm import *
from Vertex import Vertex
from PIL import Image


def save_image(shape, matrix, i):

    img = Image.new('1', shape)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = int(matrix[i][j])

    img.save(f't{i}.bmp')


def getCoordinates(indVertex, object):
    coordinates = []
    vertice = object.vertices[indVertex]

    for axis in vertice:
        coordinates.append(int(axis))

    return coordinates


def objToMatrix (x, y, object):
    matrix = np.zeros((x, y))
    
    for i, f in enumerate(object.faces):

        print(i)
        v1 = getCoordinates(f[0], object)
        v2 = getCoordinates(f[1], object)
        v3 = getCoordinates(f[2], object)

        vertex1 = Vertex(v1[0], v1[1])
        vertex2 = Vertex(v2[0], v2[1])
        vertex3 = Vertex(v3[0], v3[1])

        fill_triangle(matrix, vertex1, vertex2, vertex3)
    return matrix


# vertices, faces = ObjectLoader.load_file('objects/1face.obj')
# umaFace = Object(vertices, faces)
# matrix = objToMatrix(umaFace)

# for linha in matrix:
#     for val in linha:
#         print ('{:4}'.format(val), end=' ')
#     print()