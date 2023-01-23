class Student:
    def __init__(self, name, university, year=1):
        self.name = name
        self.university = university
        self.year = year
        self.studyy = self.year

    def get_name(self):
        return self.name

    def get_university(self):
        return self.university

    def get_year(self):
        return self.year

    def study(self):
        self.studyy += 1
        if self.studyy >= 6:
            self.studyy = 6
        self.year = self.studyy


class Employee:
    def __init__(self, name, company, position='junior'):
        self.name = name
        self.company = company
        self.position = position
        self.lstposition = ['junior', 'middle', 'senior', 'lead']

    def get_name(self):
        return self.name

    def get_company(self):
        return self.company

    def get_position(self):
        return self.position

    def work(self):
        for index, staus in enumerate(self.lstposition):
            if self.position == 'lead':
                break
            if self.position == staus:
                self.position = self.lstposition[index + 1]
                break


class Human:
    def __init__(self, name=None):
        self.name = name

    def get_name(self):
        return self.name


empl = Employee("Ivan", "Yandex")
print(empl.get_position())
empl.work()
empl.work()
print(empl.get_position())
empl.work()
empl.work()
empl.work()
print(empl.get_position())
