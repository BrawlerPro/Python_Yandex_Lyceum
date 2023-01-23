class Hyperbole:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.y = 0

    def __call__(self, other):
        if other == 0:
            return
        return round(self.a.__add__(self.b.__truediv__(other)), 6)

    def __repr__(self):
        return f'Hyp({self.a}, {self.b})'

    def __str__(self):
        return f'y = {self.a} + {self.b}/x'


hyp = Hyperbole(0.5, 1.3)
print(hyp(129))
print(hyp.__repr__())
print(hyp)
