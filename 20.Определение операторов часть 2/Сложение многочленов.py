class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, value):
        return sum([self.coefficients[i] * value ** i for i in range(len(self.coefficients))])

    def __add__(self, poly):
        poly1 = self.coefficients
        poly2 = poly.coefficients
        if len(poly1) < len(poly2):
            poly1 += [0] * (len(poly2) - len(poly1))
        else:
            poly2 += [0] * (len(poly1) - len(poly2))
        return Polynomial([poly1[i] + poly2[i] for i in range(len(poly1))])


poly1 = Polynomial([10])
poly2 = Polynomial([0, 11])
poly3 = Polynomial([0, 0, 12])

poly = poly1 + poly2 + poly3

print(poly(-10))
print(poly(-2))
print(poly(-1))
print(poly(0))
print(poly(1))
print(poly(2))
print(poly(10))
