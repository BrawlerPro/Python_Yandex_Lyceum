class FlowingRectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.coef = width / height

    def __add__(self, other):
        coef = self.coef
        cons = 0
        disc = cons ** 2 - 4 * coef * (-((self.width * self.height) + (other.width * other.height)))
        if disc > 0:
            x1 = (-cons + disc ** 0.5) / (2 * coef)
            x2 = (-cons - disc ** 0.5) / (2 * coef)
            if x1 > x2:
                side = x1
            else:
                side = x2
        elif disc == 0:
            side = -cons / (2 * coef)
        else:
            side = 0
        if side != 0:
            self.width = side * self.coef
            self.height = side
        else:
            self.width = 0
            self.height = 0

    def __sub__(self, other):
        coef = self.coef
        cons = 0
        disc = (cons ** 2) - (4 * coef * (-((self.width * self.height) - (other.width * other.height))))
        if disc > 0:
            x1 = (-cons + disc ** 0.5) / (2 * coef)
            x2 = (-cons - disc ** 0.5) / (2 * coef)
            if x1 > x2:
                side = x1
            else:
                side = x2
        elif disc == 0:
            side = -cons / (2 * coef)
        else:
            side = 0
        if side != 0:
            self.width = side * self.coef
            self.height = side
        else:
            self.width = 0
            self.height = 0

    def get_width(self):
        return round(self.width, 2)

    def get_height(self):
        return round(self.height, 2)


fr_1 = FlowingRectangle(12, 5)
fr_2 = FlowingRectangle(60, 3)
fr_1 - fr_2
print(fr_1.get_width(), fr_1.get_height())
fr_1 + fr_2
print(fr_1.get_width(), fr_1.get_height())