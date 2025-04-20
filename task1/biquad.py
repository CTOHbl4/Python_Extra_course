a, b, c = eval(input()) 
if a==b==c==0:
    print(-1)
elif a==b==(not c)==0:
    print(0)
elif a==0 and b!=0:
    if c*b > 0:
        print(0)
    else:
        if c != 0:
            print(-(-c/b)**0.5, (-c/b)**0.5)
        else:
            print(0)
elif a!=0:
    d = b*b - 4*a*c
    if d < 0:
        print(0)
    x1 = (-b - d**0.5)/2/a
    x2 = (-b + d**0.5)/2/a
    if x1 == x2 > 0:
        print(-(x2**0.5), x2**0.5)
    elif x1 == x2 == 0:
        print(0)
    elif x2 < 0:
        print(0,)
    elif x1 < 0:
        if x2 == 0:
            print(0,)
        else:
            print(-(x2**0.5), x2**0.5)
    else:
        if x1 == 0:
            print(-(x2**0.5), 0, x2**0.5)
        else:
            print(-(x2**0.5), -(x1**0.5), x1**0.5, x2**0.5)
