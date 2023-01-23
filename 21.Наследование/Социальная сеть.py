class User:
    def __init__(self, name):
        self.name = name

    def info(self):
        return ''

    def describe(self):
        print('{0}\n{1}'.format(self.name, self.info))

    def send_message(self, user, message):
        pass

    def post(self, message):
        pass


class Person(User):
    def __init__(self, name, date):
        super().__init__(name)
        self.date = date

    def info(self):
        return 'Дата рождения: {0}'.format(self.date)

    def subscribe(self, user):
        pass


class Community(User):
    def __init__(self, name, opisaniye):
        super().__init__(name)
        self.description = opisaniye

    def info(self):
        return 'Описание: {0}'.format(self.description)
