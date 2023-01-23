import math


class QuickFactorial:

    def result(self, x):
        x = math.factorial(x)
        return x


q = QuickFactorial()
print(q.result(30))
