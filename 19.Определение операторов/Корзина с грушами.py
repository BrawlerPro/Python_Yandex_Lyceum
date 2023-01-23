class PearsBasket:
    def __init__(self, onepiecesushestyuet):
        self.number = onepiecesushestyuet

    def __floordiv__(self, delitel):
        banka = []
        result = self.number // delitel
        if result < 0:
            result = 0
        num = self.number
        for i in range(delitel):
            banka.append(PearsBasket(result))
            num -= result
        if num > 0:
            banka.append(PearsBasket(num))
        return banka

    def __mod__(self, n):
        a = self.number // n
        logick = a * n
        return self.number - logick

    def __add__(self, other):
        return PearsBasket(self.number + other.number)

    def __sub__(self, other):
        if self.number - other < 0:
            self.number = 0
            return self.number
        self.number = self.number - other
        return self.number

    def __str__(self):
        return f'{self.number}'

    def __repr__(self):
        return f'PearsBasket({self.number})'


pb_1 = PearsBasket(19)
array = pb_1 // 3
print(array)
print(pb_1)
pb_2 = PearsBasket(11110)
print(pb_2 % 19)
pb_3 = pb_1 + pb_2
print([pb_3])
print(pb_3 // 6)
print(pb_3 % 7)
pb_1 - 172
print(pb_1)
print(*pb_2 // 4)
