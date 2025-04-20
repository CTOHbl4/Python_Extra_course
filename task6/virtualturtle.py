def turtle(coord, direction):
    move = yield coord
    c = list(coord)
    while move:
        if move == "f":
            if direction == 0:
                c[0] += 1
            if direction == 1:
                c[1] += 1
            if direction == 2:
                c[0] -= 1
            if direction == 3:
                c[1] -= 1
            coord = tuple(c)
            move = yield coord
        elif move == "l":
            direction = (direction + 1) % 4
            move = yield coord
        elif move == "r":
            direction = (direction - 1) % 4
            move = yield coord
