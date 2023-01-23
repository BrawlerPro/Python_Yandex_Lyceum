class Robot:
    def __init__(self, x):
        self.history = []
        x, y = x
        self.cords = x, y
        self.east = 1
        self.south = 1
        self.west = 1
        self.north = 1
        self.history.append(self.cords)

    def move(self, keyword):
        for letter in keyword:
            if letter == 'N':
                x, y = self.cords
                y += 1
                self.cords = x, y
                self.history.append(self.cords)
            if letter == 'E':
                x, y = self.cords
                x += 1
                self.cords = x, y
                self.history.append(self.cords)
            if letter == 'S':
                x, y = self.cords
                y -= 1
                self.cords = x, y
                self.history.append(self.cords)
            if letter == 'W':
                x, y = self.cords
                x -= 1
                self.cords = x, y
                self.history.append(self.cords)
        return self.cords

    def path(self):
        histor = self.history
        self.history = [histor[-1]]
        return histor


r = Robot((0, 0))
print(r.move('NENWEE'))
print(*r.path())
print()
print(r.move('ENWEWSNN'))
print(*r.path())
print()
print(r.move('NNNNNNNSSWENWEWSNN'))
print(*r.path())