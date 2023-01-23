class SparseArray:
    def __init__(self):
        self.lst = {}

    def __setitem__(self, key, value):
        self.lst[key] = value
        return

    def __getitem__(self, key):
        if key not in self.lst:
            return 0
        return self.lst[key]


arr = SparseArray()
arr[1] = 10
arr[8] = 20
for i in range(10):
    print('arr[{}] = {}'.format(i, arr[i]))