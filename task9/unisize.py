class Dsc:
    def __get__(sel, obj, cls):
        if getattr(obj, "_size", None) is not None:
            return obj._size
        if getattr(obj, "_size", None) is not None:
            return obj.def_size

        if "__len__" in obj.__dir__():
            obj.def_size = len(obj)
        elif "__abs__" in obj.__dir__():
            obj.def_size = abs(obj)
        else:
            obj.def_size = 0
        return obj.def_size

    def __set__(self, obj, value):
        obj._size = value

    def __delete__(self, obj):
        del obj._size


def sizer(cls):
    # inheritance works longer than just assignment.
    cls.size = Dsc()
    return cls
