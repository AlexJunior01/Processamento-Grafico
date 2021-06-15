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
t.create_image((1080, 1080), matrix, "cubo_final")

vertices, faces = ObjectLoader.load_file('objects/coarseTri.hand.obj')
hand = Object(vertices, faces)
hand.scale([2, 2, 2])
camera = Camera(np.array([-500, 0, 500]), np.array([0, 0, 0]))
m = camera.view_matrix
handView = t.world_to_view(m, hand)
projection = perspective(500, 500, 1, 500)
handFinal = t.world_to_view(projection, handView)
handWindow = t.view_port(handFinal, 1080, 1080)
matrix = obj_to_matrix(1080, 1080, handWindow)
t.create_image((1080, 1080), matrix, "hand_final")