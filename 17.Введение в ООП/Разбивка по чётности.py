class OddEvenSeparator:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def even(self):
        even = []
        for num in self.numbers:
            if num / 2 == num // 2:
                even.append(num)
        return even

    def odd(self):
        odd = []
        for num in self.numbers:
            if num / 2 == num // 2:
                pass
            else:
                odd.append(num)
        return odd


separator = OddEvenSeparator()
separator.add_number(1)
separator.add_number(5)
separator.add_number(6)
separator.add_number(8)
separator.add_number(3)
print(' '.join(map(str, separator.even())))
print(' '.join(map(str, separator.odd())))
