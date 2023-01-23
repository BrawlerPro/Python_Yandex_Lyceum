class Selector:
    def __init__(self, valuess):
        self.values = list(valuess)

    def get_odds(self):
        oddss = []
        for numbers in self.values:
            if numbers / 2 == numbers // 2:
                pass
            else:
                oddss.append(numbers)
        return oddss

    def get_evens(self):
        evenss = []
        for numbers in self.values:
            if numbers / 2 == numbers // 2:
                evenss.append(numbers)
            else:
                pass
        return evenss
