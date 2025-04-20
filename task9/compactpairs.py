import string


class Pairs:
    __slots__ = [letter for letter in string.ascii_letters]

    def __init__(self, N):
        for name in string.ascii_letters:
            setattr(self, name, N)
            N = (N + 1) % 52

    def __repr__(self):
        res1 = ""
        res2 = ""
        flag = True
        for name in string.ascii_letters:
            if getattr(self, name) == 1:
                flag = False
            if flag:
                res2 += name + " "
            else:
                res1 += name + " "
        return res1 + res2[:-1]
