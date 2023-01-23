inpt = input()
words_list = inpt.split()
word_start, *words, word_end = words_list
output = []

for word in words:
    if word_start.lower() <= word.lower() <= word_end.lower():
        output.append(word)

print(*output)