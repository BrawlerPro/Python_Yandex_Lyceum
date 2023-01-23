class FastFibonacci:
    def __init__(self):
        self.fibonachi = {0: 0, 1: 1}

    def __call__(self, value):
        def fib(n):
            if n in self.fibonachi:
                return self.fibonachi[n]
            self.fibonachi[n] = fib(n - 1) + fib(n - 2)
            return self.fibonachi[n]

        return fib(value)


ff = FastFibonacci()
print(ff(6))
