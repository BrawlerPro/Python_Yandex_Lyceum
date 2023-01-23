class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.c + self.b


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, side)


t = Triangle(1, 2, 3)
print(t.perimeter())
