import Model.Model


class Service:
    def __init__(self, l=[]):
        self._l = list(l)

    def __len__(self):
        return len(self._l)

    def __str__(self):
        return str(self._l)

    def __repr__(self):
        return repr(self._l)

    def add(self, value):
        self._l.append(value)

    def __setitem__(self, key, value):
        self._l[key] = value

    def __getitem__(self, item):
        if isinstance(item, slice):
            return item(self._l)
        elif isinstance(item, tuple):
            return [self._l[x] for x in item]
        elif item == Ellipsis:
            return self._l.copy()
        else:
            return self._l[item]

    def __contains__(self, item):
        return item in self._l

    def __iter__(self):
        for i in self._l:
            yield i

    def get_all_games(self):
        return list(self._l)

