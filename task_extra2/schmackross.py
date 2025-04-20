import re
from functools import wraps
import inspect
import dis


class macro:

    reg = re.compile(r"(\w+)\(([^\(\)]+)\)")
    macros = {}

    def __init__(self, *args):
        self.func = None
        if len(args):
            self.func = args[0]
            macro.macros[self.func.__name__] = self.parse_source()

    def __call__(self, *args):
        if (self.func is None) and callable(args[0]):
            # @macro()
            # change body of function
            self.func = args[0]
            source = inspect.getsource(self.func)
            start_search = 0
            while finds := macro.reg.search(source, start_search):
                # name and parameters in gr
                gr = finds.groups()
                f_name = gr[0]
                f_params = gr[1].split(",")
                if f_name in macro.macros:
                    # found macros
                    sign = macro.macros[f_name]["sign"]
                    params = {name: val for name, val in sign.items()}
                    for i, param in enumerate(f_params):
                        if "=" in param:
                            param = param.split("=")
                            params[param[0]] = "(" + param[1] + ")"
                        else:
                            params[list(params.keys())[i]] = "(" + param + ")"

                    for name, val in params.items():
                        if isinstance(val, inspect.Parameter):
                            # did not have a value to assign
                            params[name] = "(" + str(val.default) + ")"

                    expr = macro.macros[f_name]["expr"]
                    for name, value in params.items():
                        expr = expr.replace(name, value)

                    source = source.replace(source[finds.span()[0]:
                                                   finds.span()[1]],
                                            "(" + expr + ")", 1)
                start_search = finds.span()[1]

            gl = {}
            exec(source[source.find("def"):], gl)
            # redefine existing function with a newly compiled one
            return wraps(self.func)(gl[self.func.__name__])
            # return self.func
        else:
            # @macro call
            return self.func(*args)

    def parse_source(self):
        source = inspect.getsource(self.func)
        expr = source[source.find("return") + 6:].strip()
        sign = inspect.signature(self.func).parameters
        return {"expr": expr, "sign": sign}
