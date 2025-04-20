x, y, z = eval(input())
maxx = x
maxy = y
maxz = z
minx = x
miny = y
minz = z

while (s := input()):
    x, y, z = eval(s)
    if x > maxx:
        maxx  = x
    elif x < minx:
        minx = x
    if y > maxy:
        maxy  = y
    elif y < miny:
        miny = y
    if z > maxz:
        maxz  = z
    elif z < minz:
        minz = z
print((maxx - minx)*(maxy - miny)*(maxz-minz))
    
