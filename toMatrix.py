import numpy as np
from Object import Object
from ObjectLoader import ObjectLoader

def plotLineLow(x0, y0, x1, y1, matrix):
    dx = x1 - x0
    dy = y1 - y0
    yi = 1
    if dy < 0:
        yi = -1
        dy = -dy

    D = (2 * dy) - dx
    y = y0


    for x in range (x0, x1):
        matrix[x][y] = 1
        if D > 0:
            y = y + yi
            D = D + (2 * (dy - dx))
        else:
            D = D + 2 * dy


def plotLineHigh(x0, y0, x1, y1, matrix):
    dx = x1 - x0
    dy = y1 - y0
    xi = 1
    if dx < 0:
        xi = -1
        dx = -dx

    D = (2 * dx) - dy
    x = x0

    for y in range(y0, y1):
        matrix[x][y] = 1
        if D > 0:
            x = x + xi
            D = D + (2 * (dx - dy))
        else:
            D = D + 2*dx


def bresenham(firstVertex, lastVertex , matrix):
    x0 = firstVertex[0]
    y0 = firstVertex[1]
    x1 = lastVertex[0]
    y1 = lastVertex[1]
    
    if abs(y1 - y0) < abs(x1 - x0):
        if x0 > x1:
            plotLineLow(x1, y1, x0, y0, matrix)
        else:
            plotLineLow(x0, y0, x1, y1, matrix)
    else:
        if y0 > y1:
            plotLineHigh(x1, y1, x0, y0, matrix)
        else:
            plotLineHigh(x0, y0, x1, y1, matrix)


def getCoordinates(indVertex, object):
    coordinates = []
    vertice = object.vertices[indVertex]

    for axis in vertice:
        coordinates.append(int (axis))

    return coordinates

def objToMatrix (x, y, object):
    matrix = np.zeros((x, y))
    
    for f in object.faces:
        vertex1 = getCoordinates(f[0], object)
        vertex2 = getCoordinates(f[1], object)
        vertex3 = getCoordinates(f[2], object)
               
        bresenham(vertex1, vertex2, matrix)
        bresenham(vertex1, vertex3, matrix)
        bresenham(vertex2, vertex3, matrix)

    return matrix


# vertices, faces = ObjectLoader.load_file('objects/1face.obj')
# umaFace = Object(vertices, faces)
# matrix = objToMatrix(umaFace)

# for linha in matrix:
#     for val in linha:
#         print ('{:4}'.format(val), end=' ')
#     print()