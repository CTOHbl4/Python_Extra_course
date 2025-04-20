class AnnoDoc(type):
    def __init__(cls, name, parents, ns, **kwds):
        st = list()
        if "__annotations__" not in ns:
            ns["__annotations__"] = {}
        if cls.__doc__ is None:
            cls.__doc__ = ""
        for name, val in ns["__annotations__"].items():
            if isinstance(val, str):
                cls.__doc__ += f"\n{name}: {val}"
            if name not in ns:
                st.append(name)
            else:
                ns["__annotations__"][name] = type(ns[name])
        for s in st:
            del ns["__annotations__"][s]
        if len(cls.__doc__) and cls.__doc__[0] == "\n":
            cls.__doc__ = cls.__doc__[1:]
        elif not len(cls.__doc__):
            cls.__doc__ = None
        return super().__init__(name, parents, ns)
