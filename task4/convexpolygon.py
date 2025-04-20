import math

lst = []

sm0 = 0
sm1 = 0
while s := input():
    a, b = eval(s)
    sm0 += a
    sm1 += b
    lst.append([a, b])

sm0 /= len(lst)
sm1 /= len(lst)

for i in range(len(lst)):
    lst[i][0] -= sm0
    lst[i][1] -= sm1

lst = sorted(lst, key=lambda x: math.atan2(x[1], x[0]))

for i in range(len(lst)):
    v1 = lst[i]
    v2 = lst[i-1]
    v3 = lst[(i+1)%len(lst)]
    angle = -math.atan2(v3[1]-v1[1], v3[0]-v1[0]) + math.atan2(v2[1]-v1[1], v2[0]-v1[0])
    angle *= 180/math.pi
    if angle < 0:
        angle += 360

    if angle <= 0 or angle >= 180:
        print("False")
        break
else:
    print("True")
