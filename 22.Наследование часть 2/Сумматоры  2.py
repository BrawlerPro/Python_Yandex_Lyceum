class Summator:
    def transform(self, n):
        return n

    def sum(self, n):
        sm = 0
        for i in range(1, n + 1):
            sm += self.transform(i)
        return sm


class PowerSummator(Summator):
    def __init__(self, b):
        self.b = b

    def transform(self, n):
        return n ** self.b


class SquareSummator(PowerSummator):
    def __init__(self):
        super().__init__(2)

    def transform(self, n):
        return n ** self.b


class CubeSummator(PowerSummator):
    def __init__(self):
        super().__init__(3)

    def transform(self, n):
        return n ** self.b
