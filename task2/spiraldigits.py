farw, farh = eval(input())
N, M = farh, farw
loww = 0
lowh = 0

# число смен направления
max_iter = min(farw, farh)*2

# информация о направлениях
dir_lst = []
while len(dir_lst) < max_iter:
    dir_lst.append(((1, lowh), (loww, farw, 1)))
    lowh += 1
    dir_lst.append(((0, farw-1), (lowh, farh, 1)))
    farw -= 1
    dir_lst.append(((1, farh-1), (farw-1, loww-1, -1)))
    farh -= 1
    dir_lst.append(((0, loww), (farh-1, lowh-1, -1)))
    loww += 1

matr = [[0]*(M) for _ in range(N)]
counter = 0

for it in range(max_iter):
    dir = dir_lst[it]
    fixed = dir[0]
    rng_params = dir[1]
    if fixed[0]:
        for j in range(*rng_params):
            matr[fixed[1]][j] = counter
            counter = (counter+1)%10
    else:
        for j in range(*rng_params):
            matr[j][fixed[1]] = counter
            counter = (counter+1)%10
    

for i in matr:
    print(*i)
    