flag = True
mx = 0
while s := input():
    for w in s.split():
        if w.isdigit() or w.startswith('-') and w[1:].isdigit():
            i = int(w)
            if flag:
                mx = i
                flag = False
            elif i > mx:
                mx = i
print(mx)
