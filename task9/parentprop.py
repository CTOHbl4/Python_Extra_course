class Sire:
    @property
    def parent(self):
        return type(self).__mro__[1].__name__
