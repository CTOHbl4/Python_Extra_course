class NegExt:
    def __neg__(self):
        self.cur_type = type(self).__mro__[0]
        self.real_type = type(self).__mro__[2]
        self.neg = getattr(self.real_type(), "__neg__", None)
        self.slicing = getattr(self.real_type(), "__getitem__", None)
        if self.neg:
            return self.cur_type(self.real_type.__neg__(self))
        if self.slicing:
            try:
                res = self.cur_type(self.real_type.__getitem__(self, slice(1, -1)))
                return res
            except Exception:
                return self.cur_type(self)
        return self.cur_type(self)
