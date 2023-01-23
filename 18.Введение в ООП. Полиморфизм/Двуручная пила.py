class TwoHandedSawUp:
    def __init__(self, data):
        self.dat = data

    def sawing(self):
        maxn = sorted(self.dat, reverse=True)[len(self.dat) // 2:][::-1]
        minn = sorted(self.dat, reverse=True)[:len(self.dat) // 2][::-1]
        spisok = []
        for index in range(len(maxn)):
            try:

                spisok.extend([maxn[index], minn[index]])
            except IndexError:
                spisok.append(maxn[index])
        self.dat = spisok

    def get_list(self):
        return self.dat


class TwoHandedSawDown:
    def __init__(self, data):
        self.dat = data

    def sawing(self):
        maxn = sorted(self.dat)[len(self.dat) // 2:][::-1]
        minn = sorted(self.dat)[:len(self.dat) // 2][::-1]
        spisok = []
        for index in range(len(maxn)):
            try:

                spisok.extend([maxn[index], minn[index]])
            except IndexError:
                spisok.append(maxn[index])
        self.dat = spisok

    def get_list(self):
        return self.dat


def print_hist(array):
    for _ in array:
        print("*" * _)


arr = [8, 6, 1, 2, 7, 4, 5, 3, 9, 0]
thsu = TwoHandedSawUp(arr)
thsu.sawing()
print(*thsu.get_list())

thsd = TwoHandedSawDown(arr)
thsd.sawing()
print(*thsd.get_list())
