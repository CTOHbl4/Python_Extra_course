class Cooked:

    def __setattr__(self, name, val):
        annot = self.__annotations__
        if (name in annot) and callable(annot[name]):
            self.__dict__[name] = annot[name](val)
        else:
            self.__dict__[name] = val

    def __repr__(self):
        dct = self.__annotations__.copy()
        for name in self.__annotations__:
            if name in self.__dict__:
                dct[name] = self.__dict__[name]
            else:
                del dct[name]

        return ":" + " ".join([f"{name}={value}" for name, value in dct.items()]) + ":"
