res = 1
cur = 1
prev = int(input())
while i := int(input()):
    if prev <= i:
        cur += 1
    else:
        if cur > res:
            res = cur
        cur = 1
    prev = i

if cur > res:
    res = cur
print(res)