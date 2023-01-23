class A:
    def __str__(self):
        return f'A.__str__ method'

    def hello(self):
        print('Hello')


class B:
    def __str__(self):
        return f'B.__str__ method'

    def good_evening(self):
        print('Good evening')


class C(A, B):
    pass


class D(B, A):
    def __init__(self):
        self.f = 0


def new_method(arg):
    return  "new method"

def new_method2(arg):
    return "new method 2"


A.__str__ = new_method
B.__str__ = new_method2
c = C()
c.hello()
c.good_evening()
d = D()
d.hello()
d.good_evening()
print(isinstance(c, A), isinstance(c, B))
print(isinstance(d, A), isinstance(d, B))
print(c)
print(d)
