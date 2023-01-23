class LeftParagraph:

    def __init__(self, dlin):
        self.granitsa = dlin
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        strocka = ''
        for word in self.words:
            if not strocka:
                strocka += word
            elif len(strocka) + len(word) + 1 <= self.granitsa:
                strocka += ' ' + word
            else:
                print(strocka)
                strocka = word
        print(strocka)
        self.words.clear()


class RightParagraph:

    def __init__(self, dlin):
        self.granitsa = dlin
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def end(self):
        line = ''
        for word in self.words:
            if not line:
                line += word
            elif len(line) + len(word) + 1 <= self.granitsa:
                line += ' ' + word
            else:
                print(line.rjust(self.granitsa, ' '))
                line = word
        print(line.rjust(self.granitsa, ' '))
        self.words.clear()


lp = LeftParagraph(8)
lp.add_word('abc')
lp.add_word('defg')
lp.add_word('hi')
lp.add_word('jklmnopq')
lp.add_word('r')
lp.add_word('stuv')
lp.end()
print()

rp = RightParagraph(8)
rp.add_word('abc')
rp.add_word('defg')
rp.add_word('hi')
rp.add_word('jklmnopq')
rp.add_word('r')
rp.add_word('stuv')
rp.end()
print()