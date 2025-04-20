import asyncio


class Seq:
    real_order = []

    def __init__(self, name):
        self.name = name
        self.idx = len(Seq.real_order)
        Seq.real_order.append(asyncio.Event())
        if self.idx == 0:
            Seq.real_order[0].set()

    async def run(self):
        await Seq.real_order[self.idx].wait()
        Seq.real_order[(self.idx + 1) % len(Seq.real_order)].set()
        print(self.name)
        return self.name
