import transformations as t
import numpy as np


class Camera:
    def __init__(self, position, look_at):
        self._position = position
        self._look_at = look_at
        self._view_matrix = self._create_view_matrix()

    def _create_view_matrix(self):
        view_up = self._position + [0, 1, 0]
        T = np.identity(4)
        T[0][3] = -self._position[0]
        T[1][3] = -self._position[1]
        T[2][3] = -self._position[2]

        n = self._look_at - self._position
        n = n / t.get_vector_length(n)
        u = t.cross_product(view_up, n)
        u = u / t.get_vector_length(u)
        v = t.cross_product(n, u)

        R = np.identity(4)
        R[0][0:3] = u
        R[1][0:3] = v
        R[2][0:3] = n

        M = t.matrix_multiplication(R, T)
        return M

    @property
    def view_matrix(self):
        return self._view_matrix
