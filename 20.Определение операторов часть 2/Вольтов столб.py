class VoltaicPile:
    def __init__(self, lst):
        self.lst = lst
        self.position = 0
        self.volte = 0

    def __getitem__(self, key):
        return self.lst[key]

    def __setitem__(self, key, value):
        self.lst[key] = value

    def __iter__(self):
        return iter(self.lst)

    def __len__(self):
        return len(self.lst)

    def __next__(self):
        o = self.lst[self.position]
        self.position += 1
        return o

    def __str__(self):
        a = 0
        b = 0
        c = 0
        for i in self.lst:
            if i == 'Cu':
                a += 1
            if i == 'cloth':
                b += 1
            if i == 'Zn':
                c += 1
        if a == c:
            self.volte = 1.1 * a
        else:
            if a < c != 0:
                self.volte = 1.1 * a
            if c < a != 0:
                self.volte = 1.1 * c
        return f'{self.volte} V'

    def append(self, value):
        if value == 'cloth':
            if self.lst[-1] == 'Cu':
                self.lst.append(value)
            if self.lst[-1] == 'Zn':
                self.lst.append(value)
        if len(self.lst) == 0:
            self.lst.append(value)
        if len(self.lst) < 2:
            if value == 'Zn':
                if self.lst[-1] == 'cloth':
                    self.lst.append(value)
            if value == 'Cu':
                if self.lst[-1] == 'cloth':
                    self.lst.append(value)
        else:
            if value == 'Zn':
                if self.lst[-1] == 'cloth' and self.lst[-2] == 'Cu':
                    self.lst.append(value)
            if value == 'Cu':
                if self.lst[-1] == 'cloth' and self.lst[-2] == 'Zn':
                    self.lst.append(value)


vp = VoltaicPile([])
for item in ['Cu', 'cloth', 'Zn', 'cloth', 'Cu', 'Zn', 'cloth', 'Cu', 'Zn',
             'cloth', 'Cu', 'Zn', 'cloth', 'Cu', 'Zn', 'cloth', 'Cu', 'Zn']:
    vp.append(item)
print(*vp)
print(vp)
