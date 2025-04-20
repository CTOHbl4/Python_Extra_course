def squares(w, h, *args):
    mtr = [["."]*w for _ in range(h)]
    for j0, i0, size, c in args:
        for i in range(i0, i0+size):
            for j in range(j0, j0+size):
                mtr[i][j] = c
    for l in mtr:
        print("".join(l))
