class Profile:
    def __init__(self, prof):
        self.prof = prof

    def info(self):
        return ''

    def describe(self):
        print(self.prof, self.info())


class Vacancy(Profile):
    def __init__(self, pro, dat):
        super().__init__(pro)
        self.dat = dat

    def info(self):
        return f'Предлагаемая зарплата: {self.dat}'


class Resume(Profile):
    def __init__(self, pro, dat):
        super().__init__(pro)
        self.dat = dat

    def info(self):
        return f'Стаж работы: {self.dat}'