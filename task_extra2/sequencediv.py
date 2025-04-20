import ast


class SuperDivSubst(ast.NodeTransformer):
    """AST transformer a//b → superDiv(a, b)."""

    def visit_BinOp(self, node):
        """Substitute ast.FloorDiv with ast.Call(SuperDiv)."""
        if isinstance(node.op, ast.FloorDiv):
            nnode = ast.Call(func=ast.Name(id='superDiv', ctx=ast.Load()),
                            args=[node.left, node.right], keywords=[])
            ast.fix_missing_locations(nnode)
            print(ast.unparse(nnode))
            return nnode
        return node


def superDiv(a, b):
    if getattr(a, "__floordiv__", None):
        return a // b
    return a[:len(a)//b]


substr = SuperDivSubst()
lc = {"superDiv": superDiv}
try:
    while s := input():
        s = ast.parse(s)
        gen = ast.walk(s)
        for i in gen:
            if isinstance(i, ast.BinOp) and isinstance(i.op, ast.FloorDiv):
                # if write i = Call(...), than we simply reassign i and lose information.
                # thus a hack.
                i.__dict__ = {"func":ast.Name(id='superDiv', ctx=ast.Load()),
                                    "args":[i.left, i.right], "keywords":[]}
                i.__class__ = ast.Call
        exec(ast.unparse(s), globals(), lc)
except EOFError:
    "end of input"
