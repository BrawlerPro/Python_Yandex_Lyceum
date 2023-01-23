def new_print(text):
    words = text.split()
    lst = []
    for word in words:
        lst.append(word.upper)
    print(' '.join(lst))


new_print(input())