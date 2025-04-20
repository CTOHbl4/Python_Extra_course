N = 100
counter = [[0]*N for _ in range(N)]

while s := input():
    a, b = eval(s)
    counter[a-1][b-1] += 1

for i in range(N):
    for j in range(N):
        e = counter[i][j]
        for _ in range(e):
            print(i+1, j+1, sep=", ")
