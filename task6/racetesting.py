from itertools import cycle


def speed(path, stops, times):
    pth = iter(path)
    tms = iter(times)
    stps = cycle(stops)
    while 1:
        sm = 0
        i = next(stps)
        for _ in range(i):
            sm += next(pth, 0)
        t = next(tms, 0)
        if sm == 0 or t == 0:
            break
        sm /= t
        yield sm
