class BoundingRectangle:
    def __init__(self):
        self.point = []
        self.left = 0
        self.right = 0
        self.bottom = 0
        self.top = 0
        self.w = 0
        self.hi = 0

    def width(self):
        return self.widht

    def height(self):
        return self.hight

    def bottom_y(self):
        return self.bottom

    def top_y(self):
        return self.top

    def left_x(self):
        return self.left

    def right_x(self):
        return self.right

    def add_point(self, x, y):
        self.point.append([x, y])
        self.parametrs()

    def parametrs(self):
        self.left = min(self.point, key=lambda x: x[0])[0]
        self.right = max(self.point, key=lambda x: x[0])[0]
        self.bottom = min(self.point, key=lambda x: x[1])[1]
        self.top = max(self.point, key=lambda x: x[1])[1]
        self.widht = abs(self.left - self.right)
        self.hight = abs(self.bottom - self.top)


rect = BoundingRectangle()
rect.add_point(-1, -2)
rect.add_point(3, 4)
print(rect.left_x(), rect.right_x())
print(rect.bottom_y(), rect.top_y())
print(rect.width(), rect.height())
