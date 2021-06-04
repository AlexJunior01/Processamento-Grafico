from Object import Object

file_name = "coarseTri.cube.obj"
cube = Object(file_name)
cube.scale([3, 0, 0])
cube.save_file("test3.obj")
