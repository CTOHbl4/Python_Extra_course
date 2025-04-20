import asyncio


class FilterQueue(asyncio.Queue):
    @property
    def window(self):
        if self.qsize():
            return self._queue[0]
        else:
            return None

    def __contains__(self, filt):
        return len(list(filter(filt, self._queue))) > 0

    def later(self):
        obj = super().get_nowait()
        super().put_nowait(obj)

    async def get(self, filt=lambda x: True):
        if self.window is None or filt not in self:
            return await super().get()
        while not filt(self.window):
            self.later()
        return await super().get()
