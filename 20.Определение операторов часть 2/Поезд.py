class Train:
    def __init__(self, numberw, lst=None):
        if lst is None:
            lst = []
        self.num = numberw
        self.lst = lst

    def __len__(self):
        return len(self.lst)

    def __str__(self):
        return f"Train {self.num}, {len(self.lst)} вагонов"

    def __getitem__(self, key):
        return self.lst[key]

    def __setitem__(self, key, value):
        self.lst[key] = value

    def __delitem__(self, key):
        if key == len(self.lst) - 1:
            del self.lst[key]

    def __iter__(self):
        return iter(self.lst)

    def append(self, e):
        self.lst.append(e)

    def get_number(self):
        return self.num

    def get_wagons(self):
        return self.lst


class Wagon:
    def __init__(self, number):
        self.num = number

    def __str__(self):
        return f"№{self.num}"

    def get_number(self):
        return self.num
