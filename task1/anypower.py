N = int(input())
res = False
for base in range(2, int(N**0.5)+1):
    newbase = base
    while newbase < N:
        newbase *= base
    else:
        if newbase == N:
            res = True
            break
if res:
    print("YES")
else:
    print("NO")