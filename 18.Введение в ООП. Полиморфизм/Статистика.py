class MinStat:
    def __init__(self):
        self.lst = []

    def add_number(self, number=None):
        self.lst.append(number)

    def result(self):
        if not self.lst:
            return None
        return min(self.lst)


class MaxStat:
    def __init__(self):
        self.lst = []

    def add_number(self, number=None):
        self.lst.append(number)

    def result(self):
        if not self.lst:
            return None
        return max(self.lst)


class AverageStat:
    def __init__(self):
        self.lst = []

    def add_number(self, number=None):
        self.lst.append(number)

    def result(self):
        if not self.lst:
            return None
        return float(sum(self.lst)) / max(len(self.lst), 1)


mins = MinStat()
maxs = MaxStat()
average = AverageStat()

print(mins.result(), maxs.result(), average.result())