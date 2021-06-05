class ObjectLoader:
    @staticmethod
    def load_file(file_name):
        file = open(file_name, "r")
        vertices = []
        faces = []
        for line in file:
            values = line.replace("/", " ").split()

            if values[0] == 'v':
                vertex = [float(values[1]), float(values[2]), float(values[3])]
                vertices.append(vertex)
            elif values[0] == 'f':
                face = [int(values[1]) - 1, int(values[2]) - 1, int(values[3]) - 1]
                faces.append(face)
        file.close()
        return vertices, faces
