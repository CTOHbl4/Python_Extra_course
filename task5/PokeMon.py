config = {"player-deck":{}, "deck-cards":{}}

while s := input():
    info = s.split(" / ")
    if info[0].isnumeric():

        if info[0] not in config["deck-cards"].keys():
            config["deck-cards"][info[0]] = set([info[1]])
        else:
            config["deck-cards"][info[0]].add(info[1])
    else:
        if info[0] not in config["player-deck"].keys():
            config["player-deck"][info[0]] = set([info[1]])
        else:
            config["player-deck"][info[0]].add(info[1])

results = {}
player_deck = set()
for player in config["player-deck"].keys():
    for deck in config["player-deck"][player]:
        player_deck |= config["deck-cards"][deck]
    results[player] = len(player_deck)
    player_deck = set()

max_num = results[max(results, key=lambda x: results[x])]
res = []
for name in results.keys():
    if results[name] == max_num:
        res.append(name)

print(*sorted(res), sep="\n")
