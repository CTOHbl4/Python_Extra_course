import re
import fractions


def interval(diap):
    one = re.compile(r"[\(\[](-?[0-9]+(?:\.[0-9]+)?)\.\.([0-9]+)\.\.(-?[0-9]+(?:\.[0-9]+)?)[\)\]]")
    match = one.match(diap)

    if match is None:
        two = re.compile(r"[\(\[](-?[0-9]+(?:\.[0-9]+)?)(\.\.\.*)(-?[0-9]+(?:\.[0-9]+)?)[\)\]]")
        match = two.match(diap)

        if match is None:
            return []

        gr = match.groups()
        start = fractions.Fraction(gr[0])
        len_interval = len(gr[1])
        finish = fractions.Fraction(gr[2])
    else:
        gr = match.groups()
        start = fractions.Fraction(gr[0])
        len_interval = int(gr[1])
        finish = fractions.Fraction(gr[2])

    start_in = (diap[0] == "[")
    finish_in = (diap[-1] == "]")
    step = (finish - start)/(len_interval - 1)
    if step == 0:
        step = 1

    res = [start]
    while start != finish:
        start += step
        res.append(start)

    if not start_in:
        res = res[1:]
    if not finish_in:
        res = res[:-1]
    return res
