class AbstractCat:
    def __init__(self):
        self.wheight = 0
        self.fastfood = 0

    def eat(self, fastfood):
        self.fastfood += fastfood
        while True:
            if self.fastfood - 10 < 0:
                break
            else:
                self.fastfood -= 10
                if self.wheight == 100:
                    pass
                else:
                    self.wheight += 1

    def __repr__(self):
        return f'{self.__class__.__name__} ({self.wheight})'


class Kitten(AbstractCat):
    def __init__(self, weight):
        super().__init__()
        self.wheight = weight

    def meow(self):
        if self.__class__.__name__ == 'Cat':
            return 'MEOW...'
        return 'meow...'

    def sleep(self):
        weight = self.wheight
        snore = ''
        for i in range(weight // 5):
            snore = snore + 'Snore'
        return snore


class Cat(Kitten):
    def __init__(self, weight, name):
        super().__init__(weight)
        self.name = name

    def catch_mice(self):
        return 'Got it!'

    def get_name(self):
        return self.name


kit = Kitten(15)
kit.eat(24)
print(kit.sleep())
print(kit.meow())
cat = Cat(41, 'Molly')
print(cat.meow())
print(cat.catch_mice())
print(cat)
print(cat.get_name())
for i in range(2, 120, 5):
    kit.eat(i)
    cat.eat(i)
print(kit, cat)