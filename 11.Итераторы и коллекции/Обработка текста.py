text = input().split()

words = []

for word in text:
    if '.' in word:
        wrd = word.remove('.')
        words.append(wrd)
    else:
        words.append(word)

print()