class SeaMap:
    def __init__(self):
        self.cords = [['-' for _ in range(3)] for _ in range(3)]

    def shoot(self, x, y, result):
        if result == 'miss':
            self.cords[x][y] = '*'
        elif result == 'hit':
            self.cords[x][y] = 'x'
        elif result == 'sink':
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if 0 <= i < 10 and 0 <= j < 10:
                        if self.cords[i][j] == '.':
                            self.cords[i][j] = '*'
            self.cords[x][y] = 'x'
            for gor in range(len(self.cords)):
                if self.cords[x][gor] == 'x':
                    y = gor
                    for ver in range(x - 1, x + 2):
                        for gori in range(y - 1, y + 2):
                            if 0 <= ver < 10 and 0 <= gori < 10:
                                if self.cords[ver][gori] == '.':
                                    self.cords[ver][gori] = '*'
            for ver in range(len(self.cords)):
                if self.cords[ver][y] == 'x':
                    x = ver
                    for vert in range(x - 1, x + 2):
                        for gori in range(y - 1, y + 2):
                            if 0 <= vert < 10 and 0 <= gori < 10:
                                if self.cords[vert][gori] == '.':
                                    self.cords[vert][gori] = '*'

    def cell(self, x, y):
        return self.cords[x][y]


sm = SeaMap()
sm.shoot(5, 4, 'sink')
sm.shoot(5, 5, 'sink')
for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()
