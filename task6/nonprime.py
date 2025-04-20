def check_nonprime(k):
    if k % 2 == 0 and k > 2:
        return True
    for i in range(3, int(k**0.5)+1, 2):
        if k % i == 0:
            return True
    return False


def nonprime(n=0):
    k = n + 1
    if k == 1:
        yield k
        k += 1
    while k:
        if check_nonprime(k):
            yield k
        k += 1
