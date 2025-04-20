import re

restr = input()
regexp = re.compile(restr)

while s := input():
    match = re.search(regexp, s)
    if match is not None:
        start, finish = match.span()
        print(f"{start}: {s[start:finish]}")
        dictwithpos = {}
        for i, val in enumerate(match.groups()):
            if (val is not None) and val != "":
                start, finish = match.span(i+1)
                print(f"{i+1}/{start}: {val}")
        for name, val in match.groupdict().items():
            if (val is not None) and val != "":
                start, finish = match.span(name)
                print(f"{name}/{start}: {val}")
    else:
        print("<NONE>")
