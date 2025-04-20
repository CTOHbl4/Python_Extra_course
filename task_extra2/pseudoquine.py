def quine():
    import inspect
    return inspect.getsource(quine)
