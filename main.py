from Object import Object
from ObjectLoader import ObjectLoader
from Camera import Camera
import transformations as t
from Projection import *
from toMatrix import *


vertices, faces = ObjectLoader.load_file('objects/coarseTri.cube.obj')
cube = Object(vertices, faces)
cube.scale([100, 100, 100])
camera = Camera(np.array([200, 200, 200]), np.array([0, 0, 0]))
m = camera.view_matrix
cubeView = t.world_to_view(m, cube)
projection = perspective(100, 100, 1, 300)
cubeFinal = t.world_to_view(projection, cubeView)
cubeWindow = t.view_port(cubeFinal, 1080, 1080)
matrix = obj_to_matrix(1080, 1080, cubeWindow)
t.create_image((1080, 1080), matrix, "teste_final")
