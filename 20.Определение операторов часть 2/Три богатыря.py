def rsort(name, vin, weapon):
    return vin, len(weapon), len(name)


def resort(vin, weapon):
    return vin, len(weapon)


def namesort(name):
    return name, len(name)


class EpicHero:
    def __init__(self, name, victory, weapon):
        self.name = f'{name}'
        self.vinrade = victory
        self.weapon = weapon

    def __str__(self):
        return f'Epic Hero {self.name}, {self.vinrade}'

    def __repr__(self):
        return f"EpicHero('{self.name}', {self.vinrade}, {sorted(self.weapon)})"

    def add_win(self):
        self.vinrade += 1

    def add_weapon(self, item):
        self.weapon.append(item)

    def del_weapon(self, item):
        if item not in self.weapon:
            return
        else:
            for index, items in enumerate(self.weapon):
                if items == item:
                    self.weapon.pop(index)

    def __eq__(self, other):
        if rsort(self.name, self.vinrade, self.weapon) == rsort(other.name, other.vinrade, other.weapon):
            return True
        return False

    def __ne__(self, other):
        if rsort(self.name, self.vinrade, self.weapon) != rsort(other.name, other.vinrade, other.weapon):
            return True
        return False

    def __lt__(self, other):
        if len(self.name) > len(other.name):
            if resort(self.vinrade, self.weapon) < resort(other.vinrade, other.weapon):
                return True
        return False

    def __gt__(self, other):
        if namesort(self.name) > namesort(other.name):
            if resort(self.vinrade, self.weapon) > resort(other.vinrade, other.weapon):
                return True
        return False

    def __le__(self, other):
        if namesort(self.name) >= namesort(other.name):
            if resort(self.vinrade, self.weapon) <= resort(other.vinrade, other.weapon):
                return True
        return False

    def __ge__(self, other):
        if namesort(self.name) >= namesort(other.name):
            if resort(self.vinrade, self.weapon) >= resort(other.vinrade, other.weapon):
                return True
        return False


eh_1 = EpicHero('Ilya Muromets', 2, ['mace', 'bow'])
eh_2 = EpicHero('Dobrynya', 2, ['knife', 'sword'])
eh_3 = EpicHero('Ilya', 2, ['lash'])
print(eh_2 <= eh_1)
print(eh_1 > eh_3)
print(*[eh_1, eh_2, eh_3], sep='\n')
print(eh_1 != eh_3)
eh_1.add_win()
print(eh_1 >= eh_3)