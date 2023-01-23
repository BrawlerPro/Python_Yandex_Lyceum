class ClassicalMechanics:
    def __init__(self, velocity):
        self.velocity = velocity

    def __call__(self, y):
        v = self.velocity + y
        return v

    def __str__(self):
        return f'Object {self.__class__.__name__}, velocity {self.velocity} c'


class SpecialTheoryRelativity(ClassicalMechanics):
    def __call__(self, y):
        if self.velocity >= 0.1:
            return (self.velocity + y) / (1 + ((self.velocity * y) / 1))
        return ClassicalMechanics.__call__(self, y)
