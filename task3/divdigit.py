def divdigit(n):
    count = 0
    for i in str(n):
        ii = int(i)
        if ii and not (n % ii):
            count += 1
    return count
