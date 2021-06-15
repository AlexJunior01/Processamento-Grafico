from Object import Object
from ObjectLoader import ObjectLoader
from Camera import Camera
import numpy as np
import transformations as t
import Projection as p
import toMatrix as tm

import numpy as np
from PIL import Image

def create_image(shape, matrix):

    img = Image.new('1', shape)
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels[i, j] = int(matrix[i][j])

    img.show('teste_final.bmp')

vertices, faces = ObjectLoader.load_file('objects/coarseTri.cube.obj')
cube = Object(vertices, faces)
cube.scale([100, 100, 100])

camera = Camera(np.array([200, 200, 200]), np.array([0, 0, 0]))
m = camera._create_view_matrix()

cubeView = t.world_to_view(m, cube)

projection = p.perspective(80, 90, 1, 300)

cubeFinal = t.world_to_view(projection, cubeView)

cubeWindow = t.view_port(cubeFinal, 1900, 1000)

matrix = tm.objToMatrix(1920, 1080, cubeWindow)

# for linha in matrix:
#     for val in linha:
#         print ('{:4}'.format(val), end=' ')
#     print()

create_image((1920, 1080), matrix)

#cubeFinal.save_file('cubeFinal.obj')


#cube.save_file('teste1.obj')


