import random


def rnd(a, b=None):
    match type(a).__name__ + " " + type(b).__name__:
        case "int NoneType":
            return random.randint(0, a)
        case "int int":
            return random.randint(a, b)
        case "float int" | "float float":
            return random.random()*(b-a)+a
        case "str NoneType":
            return random.choice(a.split())
        case "str int":
            start = random.randint(0, len(a)-b)
            return a[start: start+b]
        case "str str":
            return random.choice(a.split(b))
        case default:
            types = default.split(" ")
            if types[1] == "NoneType":
                return random.choice(list(a))
            elif types[1] == "int":
                return random.choices(list(a), k=b)
