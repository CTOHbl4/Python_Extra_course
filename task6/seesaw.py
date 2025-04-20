def seesaw(it):
    even = []
    odd = []

    for i in it:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    even = even[::-1]
    odd = odd[::-1]
    while even and odd:
        yield even.pop()
        yield odd.pop()

    while even:
        yield even.pop()
    while odd:
        yield odd.pop()
