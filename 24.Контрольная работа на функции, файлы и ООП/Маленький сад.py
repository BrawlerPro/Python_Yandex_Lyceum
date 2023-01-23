def sortByAlphabet(inputStr):
    return inputStr[0]


def little_garden(*data):
    andat = []
    for index, offers in enumerate(data):
        if len(offers) > 5:
            word = []
            for t, i in enumerate(offers):
                if t % 2 == 0:
                    word.append(i.upper())
                else:
                    word.append(i)
            andat.append(''.join(word))
        else:
            if offers < 'nightingale':
                andat.append(offers[::-1])
            else:
                word2 = []
                for i in offers[::2]:
                    word2.append(i)
                andat.append(''.join(word2))
    andat = sorted(andat)
    return tuple(andat)


data = ["aar", "far", "away", "beyond", "zoooo", "pine", "forest"]
print(little_garden(*data))