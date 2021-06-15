class Vertex:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        string = 'x = {} y = {}\n'.format(self._x, self._y)
        return string

    def __repr__(self):
        return repr((self.y, self.x))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, var):
        self._x = var

    @y.setter
    def y(self, var):
        self._y = var
