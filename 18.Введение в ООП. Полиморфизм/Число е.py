import math as m


class EulerNumber:
    def __init__(self, enum):
        self.m = m
        self.enumber = enum

    def get_number(self, x=1):
        genum = 0
        for num in range(self.enumber):
            genum += (x ** num) / self.m.factorial(num)
        return genum