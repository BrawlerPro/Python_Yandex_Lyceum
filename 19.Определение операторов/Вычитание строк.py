class ModifiedString:
    def __init__(self, word):
        self.offer = word

    def __add__(self, other):
        return f'{self.offer + other}'

    def __radd__(self, other):
        return f'{other + self.offer}'

    def __sub__(self, other):
        firstsl = self.offer
        for letter in firstsl:
            if letter.lower() in other.lower():
                firstsl = firstsl.replace(letter, '')
        return f'{firstsl}'

    def __rsub__(self, other):
        secondsl = other
        for letter in secondsl:
            if letter.lower() in self.offer.lower():
                secondsl = secondsl.replace(letter, '')
        return f'{secondsl}'

    def __str__(self):
        return self.offer


ms_1 = ModifiedString('My heart in the Highland')
ms_2 = 'my heart is not here'
print(ms_1 - ms_2)
print(ms_2 - ms_1)
