import asyncio


class Monster:
    def __init__(self, name, pos, delay, power):
        self.name = name
        self.pos = pos
        self.delay = delay
        self.count_episodes = 0
        self.power = power

    async def run(self, sync_start: asyncio.Barrier, sync_end: asyncio.Barrier):
        while True:
            await sync_start.wait()
            self.count_episodes += 1
            if self.count_episodes == self.delay:
                self.pos += 1
                self.count_episodes = 0
            await sync_end.wait()


def find_left(monsters):
    dct_pos = {}
    for i, monster in enumerate(monsters):
        if monster.pos not in dct_pos.keys():
            dct_pos[monster.pos] = [i]
        else:
            dct_pos[monster.pos].append(i)
            return dct_pos[monster.pos]
    return None


def fight(monsters, idxs):
    if idxs is not None:
        id1, id2 = idxs
        monster1, monster2 = monsters[id1], monsters[id2]
        min_power = min(monster1.power, monster2.power)
        monster1.power -= min_power
        # print(monsters, id1, id2)
        if monster1.power == 0:
            monsters.pop(id1)
            id2 -= 1
        monster2.power -= min_power
        if monster2.power == 0:
            monsters.pop(id2)


def get_res(monsters, init_len):
    if len(monsters) == 0:
        return "All dead"
    elif len(monsters) == init_len:
        return "All flee"
    else:
        res = ""
        for m in monsters[:-1]:
            res += m.name + ", "
        return res + monsters[-1].name


async def game(monsters: list[Monster], sync_start: asyncio.Barrier, sync_end: asyncio.Barrier, epoch):
    init_len = len(monsters)

    for _ in range(epoch):

        if len(monsters) <= 1:
            break

        await sync_start.wait()
        await sync_end.wait()

        idxs = find_left(monsters)

        fight(monsters, idxs)

    return get_res(monsters, init_len)
