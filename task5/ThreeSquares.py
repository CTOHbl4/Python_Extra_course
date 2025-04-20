seq = set(eval(input()))

M = max(seq)
limit_i = int(M ** 0.5) + 1
target = set()

for i in range(1, limit_i):
    a = i*i
    limit_j = int((M - a)**0.5) + 1
    for j in range(i , limit_j):
        b = j*j
        limit_k = int((M - a-b)**0.5) + 1
        for k in range(j, limit_k):
            target.add(a + b + k*k)

print(len(seq & target))
