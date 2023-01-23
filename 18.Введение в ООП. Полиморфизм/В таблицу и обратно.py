class LineToTable:
    def __init__(self, lst, x, y):
        self.list = lst
        self.x = x
        self.y = y
        self.matrix = []

    def resize(self):
        for i in range(self.x):
            ur = []
            for u in range(self.y):
                o = self.list[0]
                ur.append(o)
                self.list.remove(o)
            self.matrix.append(ur)
        return self.matrix, self.x, self.y


class TableToLine:
    def __init__(self, matrixx):
        self.matrix = matrixx
        self.list = []
        self.x = 0

    def resize(self):
        for y in self.matrix:
            self.x = len(y)
            for x in y:
                self.list.append(x)
        return self.list, len(self.matrix), self.x


ltt = LineToTable([1, 2, 3, 4, 5, 6], 3, 2)
matrix, a, b = ltt.resize()
print(*matrix, sep='\n')
print(f'Sizes: {a}x{b}')

ttl = TableToLine([[1, 2], [3, 4], [5, 6]])
arr, n, m = ttl.resize()
print(arr)
print(f'Resized from {n}x{m}')
