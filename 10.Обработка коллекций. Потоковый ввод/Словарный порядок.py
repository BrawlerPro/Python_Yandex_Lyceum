words = input().split()


def lowr(word):
    return word.lower()


new_list = sorted(words, key=lowr)

print(*new_list)