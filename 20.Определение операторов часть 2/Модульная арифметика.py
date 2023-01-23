import math


class ModularArithmetic:
    def __init__(self, number, module):
        self.num = number
        self.mod = module

    def __call__(self, other):
        return other // self.mod

    def __add__(self, other):
        nsum = self.num + other.num
        if nsum > self.mod:
            for i in range(1000):
                nsum = nsum - self.mod
                if nsum < self.mod:
                    break
            return ModularArithmetic(nsum, self.mod)
        else:
            return ModularArithmetic(nsum, self.mod)

    def __sub__(self, other):
        nsum = self.num - other.num
        if nsum < 0:
            for i in range(1000):
                nsum = nsum + self.mod
                if nsum > 0:
                    break
            return ModularArithmetic(nsum, self.mod)
        else:
            return ModularArithmetic(nsum, self.mod)

    def __lshift__(self, other):  # << -
        nsum = self.num - other
        if nsum < 0:
            for i in range(1000):
                nsum = nsum + self.mod
                if nsum > 0:
                    break
            return ModularArithmetic(nsum, self.mod)
        else:
            for i in range(1000):
                nsum = nsum - self.mod
                if nsum < self.mod:
                    break
            return ModularArithmetic(nsum, self.mod)

    def __rshift__(self, other):  # >> +
        nsum = self.num + other
        if nsum > self.mod:
            for i in range(1000):
                nsum = nsum - self.mod
                if nsum < self.mod:
                    break
            return ModularArithmetic(nsum, self.mod)
        else:
            for i in range(1000):
                nsum = nsum + self.mod
                if nsum > 0:
                    break
            return ModularArithmetic(nsum, self.mod)

    def __str__(self):
        return f'{self.num.__round__()}({self.mod})'

    def __repr__(self):
        return f'{self.num.__round__()}({self.mod})'


ma_1 = ModularArithmetic(3, 12)
ma_2 = ModularArithmetic(11, 12)
ma_3 = ma_1 + ma_2
ma_4 = ma_1 - ma_2
ma_5 = ma_2 >> 541
ma_6 = ma_1 << 168
array = [ma_1 + ma_6, ma_2 >> 3464, ma_3 << -455, ma_4 - ma_2, ma_5 >> -485,
         ma_6]  # [6(12), 7(12), 1(12), 5(12), 7(12), 3(12)][6(12), 7(12), 457(12), 5(12), -485(12), 3(12)]
print(array)
