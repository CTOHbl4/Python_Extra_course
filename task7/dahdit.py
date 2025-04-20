class morse:
    def __init__(self, line="di dit dah"):
        line = line.split(" ")
        issymb = False

        if len(line) == 1:
            issymb = True
            line = line[0]
            self.lettersep = " "
            self.symsep = ""

        if len(line) == 2:
            self.dot = line[0]
            self.enddot = line[0]
            self.dash = line[1]
            self.endmess = "" if issymb else "."

        elif len(line) == 3:
            self.dot = line[0]
            self.enddot = line[1]
            self.dash = line[2]
            self.endmess = "" if issymb else "."

        elif len(line) == 4:
            self.dot = line[0]
            self.enddot = line[1]
            self.dash = line[2]
            self.endmess = line[3]

        if not issymb:
            self.lettersep = ","
            self.symsep = " "

        self.config = ""

    def __neg__(self):
        self.config = "-" + self.config
        return self

    def __pos__(self):
        self.config = "+" + self.config
        return self

    def __invert__(self):
        self.config = "~" + self.config
        return self

    def __repr__(self):
        res = ""

        if not len(self.config):
            return self.endmess

        for c in range(len(self.config)):
            if self.config[c] == "+":
                if (c <= len(self.config) - 2) and self.config[c+1] == "~":
                    res += self.enddot + self.lettersep
                elif c == len(self.config) - 1:
                    res += self.enddot + self.endmess
                else:
                    res += self.dot + self.symsep
            elif self.config[c] == "-":
                if (c <= len(self.config) - 2) and self.config[c+1] == "~":
                    res += self.dash + self.lettersep
                elif c == len(self.config) - 1:
                    res += self.dash + self.endmess
                else:
                    res += self.dash + self.symsep
            else:
                res += self.symsep
        return res
