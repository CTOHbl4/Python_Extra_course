lc = {}
while s := input():
    if s.lstrip()[0] == '#':
        continue

    if '=' not in s:
        try:
            print(eval(s, {"__builtins__": {}}, lc))
        except NameError:
            print("Name error")
        except SyntaxError:
            print("Syntax error")
        except Exception:
            print("Runtime error")

    else:
        eq = s.find('=')
        ident = s[:eq].strip()
        try:
            val = eval(s[eq+1:], {"__builtins__": {}}, lc)
        except NameError:
            print("Name error")
            continue
        except SyntaxError:
            print("Syntax error")
            continue
        except Exception:
            print("Runtime error")
            continue

        if ident.isidentifier():
            lc[ident] = val
        else:
            print("Assignment error")
