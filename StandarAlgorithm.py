import numpy as np
from Vertex import Vertex


def sort_vertices_y(v1, v2, v3):
    nova_lista = sorted([v1, v2, v3], key=lambda vertex: vertex.y)
    return nova_lista


def sort_vertices_x(v1, v2, v3):
    nova_lista = sorted([v1, v2, v3], key=lambda vertex: vertex.x)
    return nova_lista


def fill_triangle(matriz, vt1, vt2, vt3):
    vt1, vt2, vt3 = sort_vertices_y(vt1, vt2, vt3)

    if vt1.y == vt2.y == vt3.y:
        vt1, vt2, vt3 = sort_vertices_x(vt1, vt2, vt3)
        drawLine(matriz, vt3.x, vt3.y, vt1.x, vt1.y)
    elif vt2.y == vt3.y:
        fill_flat_side_triangle_int(matriz, vt1, vt2, vt3)
    elif vt1.y == vt2.y:
        fill_flat_side_triangle_int(matriz, vt3, vt1, vt2)
    elif vt1.y == vt3.y:
        fill_flat_side_triangle_int(matriz, vt2, vt1, vt3)
    else:
        x = int(vt1.x + ((vt2.y - vt1.y) / (vt3.y - vt1.y)) * (vt3.x - vt1.x))
        y = vt2.y
        vTmp = Vertex(x, y)
        fill_flat_side_triangle_int(matriz, vt1, vt2, vTmp)
        fill_flat_side_triangle_int(matriz, vt3, vt2, vTmp)


def fill_flat_side_triangle_int(matriz, v1, v2, v3):
    vTmp1 = Vertex(v1.x, v1.y)
    vTmp2 = Vertex(v1.x, v1.y)

    changed1 = False
    changed2 = False

    dx1 = np.abs(v2.x - v1.x)
    dy1 = np.abs(v2.y - v1.y)

    dx2 = np.abs(v3.x - v1.x)
    dy2 = np.abs(v3.y - v1.y)

    signx1 = int(np.sign(v2.x - v1.x))
    signx2 = int(np.sign(v3.x - v1.x))

    signy1 = int(np.sign(v2.y - v1.y))
    signy2 = int(np.sign(v3.y - v1.y))

    if dy1 > dx1:
        tmp = dx1
        dx1 = dy1
        dy1 = tmp
        changed1 = True

    if dy2 > dx2:
        tmp = dx2
        dx2 = dy2
        dy2 = tmp
        changed2 = True

    e1 = 2 * dy1 - dx1
    e2 = 2 * dy2 - dx2

    for i in range(dx1 + 1):
        if vTmp1.x < vTmp2.x:
            drawLine(matriz, vTmp1.x, vTmp1.y, vTmp2.x, vTmp2.y)
        else:
            drawLine(matriz, vTmp2.x, vTmp2.y, vTmp1.x, vTmp1.y)

        while e1 >= 0:
            if changed1:
                vTmp1.x += signx1
            else:
                vTmp1.y += signy1
            e1 = e1 - 2 * dx1

        if changed1:
            vTmp1.y += signy1
        else:
            vTmp1.x += signx1

        e1 = e1 + 2 * dy1

        while vTmp2.y != vTmp1.y:
            while e2 >= 0:
                if changed2:
                    vTmp2.x += signx2
                else:
                    vTmp2.y += signy2
                e2 = e2 - 2 * dx2

            if changed2:
                vTmp2.y += signy2
            else:
                vTmp2.x += signx2

            e2 = e2 + 2 * dy2


def drawLine(matriz, vTmp1x, vTmp1y, vTmp2x, vTmp2y):
    for i in range(vTmp1x, vTmp2x+1):
        matriz[i][vTmp1y] = 1
