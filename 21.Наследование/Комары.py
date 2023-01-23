class Mosquito:
    def __init__(self, days):
        self.days = days

    def __str__(self):
        return f'Mosquito, {self.days} days'


class MaleMosquito(Mosquito):
    def __str__(self):
        return f'MaleMosquito, {self.days} days'

    def feed(self):
        return 'nectar'

    def lives(self):
        return 'on land'

    def squeak(self):
        return 'The thin squeak of a mosquito after eating blood'


class FemaleMosquito(Mosquito):
    def __str__(self):
        return f'FemaleMosquito, {self.days} days'

    def feed(self):
        return 'blood'

    def lives(self):
        return 'on land'

    def hearing(self):
        return f"I hear and see everything on land"


class MosquitoLarva(MaleMosquito, FemaleMosquito):
    def __str__(self):
        return f'MosquitoLarva, {self.days} days'

    def feed(self):
        return 'algae'

    def lives(self):
        return 'in water'
