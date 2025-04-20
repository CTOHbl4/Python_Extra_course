class Square:

    __match_args__ = ("x", "y", "w")

    def __init__(self, x, y, w):
        self._x = x
        self._y = y
        self._w = w
        self._h = w
        self._s = self._w*self._h
        self._center = (self._x + self._w/2, self._y + self._h/2)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = val
        self._center = (self._x + self._w/2, self._y + self._h/2)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = val
        self._center = (self._x + self._w/2, self._y + self._h/2)

    @property
    def h(self):
        return self._h

    @h.setter
    def h(self, val):
        self._w = val
        self._h = val
        self._s = val * val
        self._center = (self._x + self._w/2, self._y + self._h/2)

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, val):
        self._w = val
        self._h = val
        self._s = val * val
        self._center = (self._x + self._w/2, self._y + self._h/2)

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, val):
        pass

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, val):
        # print(val) Сначала self._center + val => конкатенация туплов. Потом присваивание.
        if len(val) < 4:
            val = (*val, 0, 0)
        self._center = val[0] + val[2], val[1] + val[3]
        self._x = self._center[0] - self._w/2
        self._y = self._center[1] - self._h/2
