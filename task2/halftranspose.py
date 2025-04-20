line = eval(input())
print(line[0])
N = len(line)
matr = [line]
for i in range(1, N):
    matr.append(eval(input()))
    stack = [*matr[i][:i+1]]
    for j in range(i-1, -1, -1):
        stack.append(matr[j][i])
    print(*stack, sep=",")
