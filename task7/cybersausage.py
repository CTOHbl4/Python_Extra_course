import fractions


class Sausage:
    top = "/" + "-"*12 + "\\"
    bottom = "\\" + "-"*12 + "/"

    def __init__(self, line="pork!", v=1):
        self.ln = fractions.Fraction(v)
        self.line = line
        self.fullline = (line * (12//len(line)+1))[:12]

    def __mul__(self, num):
        return Sausage(self.line, self.ln * num)

    def __rmul__(self, num):
        return Sausage(self.line, self.ln * num)

    def __truediv__(self, num: int):
        return Sausage(self.line, self.ln/num)

    def __abs__(self):
        return self.ln if self.ln >= 0 else 0

    def __sub__(self, sub):
        res = self.ln - sub.ln
        if res < 0:
            res = 0
        return Sausage(self.line, res)

    def __add__(self, add):
        return Sausage(self.line, self.ln + add.ln)

    def assemble_line(self, rep):
        times, mod = int(self.ln), int((self.ln - self.ln.numerator//self.ln.denominator)*12) + 1
        res = rep * times
        if mod > 1 or times == 0:
            res += rep[:mod] + "|"
        return res

    def __repr__(self):
        res = ""
        res += self.assemble_line(Sausage.top) + "\n"
        res += self.assemble_line("|" + self.fullline + "|") + "\n"
        res += self.assemble_line("|" + self.fullline + "|") + "\n"
        res += self.assemble_line("|" + self.fullline + "|") + "\n"
        res += self.assemble_line(Sausage.bottom)
        return res

    def __bool__(self):
        return self.ln != 0
