from Object import Object
from ObjectLoader import ObjectLoader
import numpy as np

vertices, faces = ObjectLoader.load_file('objects/coarseTri.cube.obj')
cube = Object(vertices, faces)
cube.translate([3, 0, 0])
cube.scale([2, 2, 2])
cube.save_file('teste1.obj')
