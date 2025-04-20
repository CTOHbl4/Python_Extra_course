class vector:
    def __init__(self, seq):
        if isinstance(seq, vector):
            self.elems = seq.elems
        else:
            self.elems = seq

    def __repr__(self):
        return ":".join(list(map(str, self.elems)))

    def __add__(self, seq):
        add = vector(seq)
        return vector(list(map(lambda x: x[0]+x[1], zip(add.elems, self.elems))))

    def __radd__(self, seq):
        add = vector(seq)
        return vector(list(map(lambda x: x[0]+x[1], zip(add.elems, self.elems))))

    def __matmul__(self, seq):
        mul = vector(seq)
        return sum(list(map(lambda x: x[0]*x[1], zip(mul.elems, self.elems))))

    def __rmatmul__(self, seq):
        mul = vector(seq)
        return sum(list(map(lambda x: x[0]*x[1], zip(mul.elems, self.elems))))
