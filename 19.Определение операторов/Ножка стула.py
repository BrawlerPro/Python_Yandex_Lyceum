class ChairLeg:
    def __init__(self, number):
        self.num = number
        self.length = self.num

    def __mul__(self, other):
        self.num = self.num * other
        self.length = self.num
        return f'{self.num * other}'

    def __rmul__(self, other):
        self.num = self.num * other
        self.length = self.num
        return f'{other * self.num}'

    def _truediv__(self, other):
        self.num = self.num / other
        self.length = self.num
        return f'{self.num / other}'

    def _rtruediv__(self, other):
        self.num = other / self.num
        self.length = self.num
        return f'{other / self.num}'

    def __floordiv__(self, other):
        self.num = self.num // other
        self.length = self.num
        return f'{self.num // other}'

    def __rfloordiv__(self, other):
        self.num = other // self.num
        self.length = self.num
        return f'{other // self.num}'

    def __mod__(self, other):
        self.num = self.num % other
        self.length = self.num
        return f'{self.num % other}'

    def __rmod__(self, other):
        self.num = other % self.num
        self.length = self.num
        return f'{other % self.num}'


chl = ChairLeg(15)
chl * 3
print(chl.length)
2 * chl
print(chl.length)
print(chl % 7)
