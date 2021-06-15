from Camera import Camera
from typing import Callable
from Object import Object
from ObjectLoader import ObjectLoader
import transformations as t
import Projection as p
import numpy as np

vertices, faces = ObjectLoader.load_file('objects/coarseTri.cube.obj')
cube = Object(vertices, faces)
cube.translate([3, 0, 0])
cube.scale([2, 2, 2])

cube.save_file('inicial.obj')

camera = Camera(np.array([10, 10, 10]), np.array([3, 0, 0]))
m = camera._create_view_matrix()

cube2 = t.world_to_view(m, cube)

resultado = p.perspective(-100, 100, -50, 50)

cube2 = t.world_to_view(resultado, cube2)

cube2.save_file('teste2.obj')

