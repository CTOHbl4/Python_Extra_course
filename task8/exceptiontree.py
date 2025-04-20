class ExceptionTree:
    def __init__(self):
        globals()["Exception-1"] = type("Exception-1", (Exception,), {"n": 1})

    def __call__(self, i):
        if "Exception-"+str(i) not in globals():
            globals()["Exception-"+str(i)] = type("Exception-"+str(i), (self(i//2),), {"n": i})
        return globals()["Exception-"+str(i)]
