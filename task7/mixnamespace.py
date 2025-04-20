def mix(*objects):
    class mixnamespace:
        def __str__(self):
            res = ""
            for name in sorted(self.__dir__()):
                if name[0] != '_':
                    val = self.__getattribute__(name)
                    if not callable(val):
                        res += f"{name}={val}, "
            return res[:-2]

    res = mixnamespace()
    for obj in objects:
        if isinstance(obj, type):
            obj = obj()
        for name in obj.__dir__():
            if name[0] != '_':
                val = obj.__getattribute__(name)
                if not callable(val):
                    res.__setattr__(name, val)
    return res
