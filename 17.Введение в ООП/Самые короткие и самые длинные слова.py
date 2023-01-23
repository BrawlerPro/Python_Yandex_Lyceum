class MinMaxWordFinder:
    def __init__(self):
        self.word = []

    def add_sentence(self, words):
        words = words.split(' ')
        self.word.append(words)
        slog = []
        for words in self.word:
            while True:
                if '' in words:
                    for off in words:
                        if off == '':
                            words.remove(off)
                else:
                    break
            slog.append(words)
        self.word = slog

    def longest_words(self):
        longo = []
        long = []
        slov = []
        dlin = []
        for words in self.word:
            for sl in words:
                slov.append(sl)
        for wr in slov:
            dlin.append(len(wr))
        for sl in slov:
            if len(sl) == max(dlin):
                longo.append(sl)
        for sl in sorted(longo):
            if sl not in long:
                long.append(sl)
        return long

    def shortest_words(self):
        short = []
        slo = []
        dlin = []
        for words in self.word:
            for sl in words:
                slo.append(sl)
        for wr in slo:
            dlin.append(len(wr))
        for sl in slo:
            if len(sl) == min(dlin):
                short.append(sl)
        return sorted(short)


finder = MinMaxWordFinder()
finder.add_sentence('zzzz')
finder.add_sentence('aaaa aaaa aaaa')
finder.add_sentence('bbb bbb bbb')
finder.add_sentence('cc cc cc')
finder.add_sentence('y y y')
finder.add_sentence('d d d')
finder.add_sentence('ee ee ee')
finder.add_sentence('fff fff fff')
finder.add_sentence('gggg gggg gggg')
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))
print()

finder.add_sentence('hhhhhhhh')

print(' '.join(finder.longest_words()))
print(' '.join(finder.longest_words()))
print(' '.join(finder.shortest_words()))
print(' '.join(finder.longest_words()))