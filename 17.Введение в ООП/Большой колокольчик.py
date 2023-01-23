class BigBell:
    def __init__(self):
        self.vizov = 1

    def sound(self):
        if self.vizov / 2 == self.vizov // 2:
            print('dong')
        else:
            print('ding')
        self.vizov += 1


bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
