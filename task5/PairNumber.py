words = []
while s := input():
    s = s.split()
    words.extend(s)

res = set()
for i in range(len(words) - 1):
    pair = frozenset([words[i], words[i + 1]])
    if pair not in res:
        res.add(pair)

print(len(res))
