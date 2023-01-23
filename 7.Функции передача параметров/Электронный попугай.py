words = []


def parrot(phrase):
    if phrase in words:
        print(phrase)
    else:
        words.append(phrase)

