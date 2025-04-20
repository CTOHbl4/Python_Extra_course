from functools import wraps


class Fix:
    def __init__(self, fix):
        self.fix = fix

    def __call__(self, func):
        @wraps(func)
        def wrap(*args, **kwargs):
            args = list(args)
            for i in range(len(args)):
                if isinstance(args[i], float):
                    args[i] = round(args[i], self.fix)
            for name, val in kwargs.items():
                if isinstance(val, float):
                    kwargs[name] = round(val, self.fix)

            result = func(*args, **kwargs)
            if isinstance(result, float):
                return round(result, self.fix)
            return result
        return wrap
