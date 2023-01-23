class TypeStatistics:
    def __init__(self, lst):
        self.spisok = lst
        self.int = []
        self.float = []
        self.str = []
        self.tuple = []
        self.set = []
        self.list = []
        self.dict = []

    def type_values(self):
        cumcollection = {}
        for index, value in enumerate(self.spisok):
            if value.__class__.__name__ == 'str':
                self.str.append(value)
            if value.__class__.__name__ == 'int':
                self.int.append(value)
            if value.__class__.__name__ == 'float':
                self.float.append(value)
            if value.__class__.__name__ == 'tuple':
                self.tuple.append(value)
            if value.__class__.__name__ == 'set':
                self.set.append(value)
            if value.__class__.__name__ == 'list':
                self.list.append(value)
            if value.__class__.__name__ == 'dict':
                self.dict.append(value)
        if self.str:
            cumcollection.update({'str': self.str})
        if self.int:
            cumcollection.update({'int': self.int})
        if self.float:
            cumcollection.update({'float': self.float})
        if self.tuple:
            cumcollection.update({'tuple': self.tuple})
        if self.set:
            cumcollection.update({'set': self.set})
        if self.list:
            cumcollection.update({'list': self.list})
        if self.dict:
            cumcollection.update({'dict': self.dict})
        return cumcollection

    def type_counts(self):
        tr, nt, loat, uple, et, ls, di = 0, 0, 0, 0, 0, 0, 0
        cumcollection = {}
        for index, value in enumerate(self.spisok):
            if value.__class__.__name__ == 'str':
                tr += 1
            if value.__class__.__name__ == 'int':
                nt += 1
            if value.__class__.__name__ == 'float':
                loat += 1
            if value.__class__.__name__ == 'tuple':
                uple += 1
            if value.__class__.__name__ == 'set':
                et += 1
            if value.__class__.__name__ == 'list':
                ls += 1
            if value.__class__.__name__ == 'dict':
                di += 1
        if tr > 0:
            cumcollection.update({'str': tr})
        if nt > 0:
            cumcollection.update({'int': nt})
        if loat > 0:
            cumcollection.update({'float': loat})
        if uple > 0:
            cumcollection.update({'tuple': uple})
        if et > 0:
            cumcollection.update({'set': et})
        if ls > 0:
            cumcollection.update({'list': ls})
        if di > 0:
            cumcollection.update({'dict': di})
        return cumcollection


arr = ['Hello', 'world', 42, 351, 273.15,
       [4, 5, 6], {type(1), type('a'), type([1, 2])},
       (0, 2), {1, 2, 3}, ('a', 'b'), 911.0,
       ['0', '1', 'x', '0'],
       {1: 'A', 2: 'B', 3: 'C'},
       {'ABC', 'CBA'}, 'Pythonic way']
ts = TypeStatistics(arr)
print(*[f'{key}: {value}' for key, value in ts.type_values().items()], sep='\n')
print(ts.type_counts())