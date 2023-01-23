class Table:
    def __init__(self, yy, xx):
        self.matrix = [[0 for _ in range(xx)] for _ in range(yy)]
        self.x = xx
        self.y = yy

    def set_value(self, y, x, num):
        self.matrix[y][x] = num

    def get_value(self, y, x):
        if y in range(self.y) and x in range(self.x):
            return self.matrix[y][x]
        return

    def n_rows(self):
        return self.y

    def n_cols(self):
        return self.x

