class ReversedList:
    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, key):
        key += 1
        key *= -1
        return self.lst[key]

    def __len__(self):
        return len(self.lst)
