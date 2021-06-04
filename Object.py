import numpy as np


class Object:
    def __init__(self, file_name):
        self._vertices = []
        self._faces = []
        self._load_file(file_name)

    @property
    def vertices(self):
        return self._vertices

    def _load_file(self, file_name):
        file = open(file_name, "r")

        for line in file:
            values = line.replace("/", " ").split()

            if values[0] == 'v':
                vertex = [float(values[1]), float(values[2]), float(values[3])]
                self._vertices.append(vertex)
            elif values[0] == 'f':
                face = [int(values[1]) - 1, int(values[2]) - 1, int(values[3]) - 1]
                self._faces.append(face)
        file.close()

    def save_file(self, file_path):
        file = open(file_path, "w")
        for vertex in self._vertices:
            string = f"v {vertex[0]} {vertex[1]} {vertex[2]}\n"
            file.write(string)

        for face in self._faces:
            string = f"f {face[0] + 1} {face[1] + 1} {face[2] + 1}\n"
            file.write(string)

        file.close()

    def _linear_transformation(self, matrix):
        for k, vertex in enumerate(self._vertices):
            new_vertex = []
            for i in range(3):
                vert_aux = vertex.copy()
                vert_aux.append(1)
                new_coord = 0
                new_coord += matrix[i][i] * vert_aux[i]
                new_coord += matrix[i][3] * vert_aux[3]

                new_vertex.append(new_coord)

            self._vertices[k] = new_vertex

    def translate(self, deltas):
        identity = np.identity(4)
        identity[0][3] = deltas[0]
        identity[1][3] = deltas[1]
        identity[2][3] = deltas[2]

        self._linear_transformation(identity)

    def scale(self, deltas):
        scale_matrix = np.identity(4)
        for i in range(3):
            if deltas[i] != 0:
                scale_matrix[i][i] = deltas[i]
        self._linear_transformation(scale_matrix)
