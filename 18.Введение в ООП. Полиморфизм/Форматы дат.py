import math


class AmericanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        a = str(self.year)
        if self.month == 10:
            b = (str(math.fmod(self.month, 100)))[:2]
        else:
            b = (str(self.month / 100))[2:]
        if self.day == 10:
            c = (str(math.fmod(self.day, 100)))[:2]
        else:
            c = (str(self.day / 100))[2:]
        dat = [b, c, a]
        return '.'.join(dat)


class EuropeanDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def set_year(self, year):
        self.year = year

    def set_month(self, month):
        self.month = month

    def set_day(self, day):
        self.day = day

    def get_year(self):
        return self.year

    def get_month(self):
        return self.month

    def get_day(self):
        return self.day

    def format(self):
        a = str(self.year)
        if self.month == 10:
            b = (str(math.fmod(self.month, 100)))[:2]
        else:
            b = (str(self.month / 100))[2:]
        if self.day == 10:
            c = (str(math.fmod(self.day, 100)))[:2]
        else:
            c = (str(self.day / 100))[2:]
        dat = [c, b, a]
        return '.'.join(dat)


american = AmericanDate(2000, 14, 10)
european = EuropeanDate(2000, 31, 10)
print(american.format())
print(european.format())
print(american.get_month())
