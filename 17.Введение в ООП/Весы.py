class Balance:
    def __init__(self):
        self.mass = 0
        self.massa = 0

    def add_right(self, massa):
        self.mass += massa

    def add_left(self, massa):
        self.massa += massa

    def result(self):
        left = self.massa
        right = self.mass
        if left > right:
            return 'L'
        if left < right:
            return 'R'
        if left == right:
            return '='


balance = Balance()
balance.add_right(10)
balance.add_left(5)
balance.add_left(5)
print(balance.result())
balance.add_left(1)
print(balance.result())
