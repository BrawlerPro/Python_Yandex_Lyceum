class Summator:
    def transform(self, n):
        return n

    def sum(self, n):
        sm = 0
        for i in range(1, n + 1):
            sm += self.transform(i)
        return sm


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3
