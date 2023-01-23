last_phrase = ['qweewqqweewq']


def print_without_duplicates(message):
    if message == last_phrase[0]:
        return
    else:
        print(message)
        last_phrase.clear()
        last_phrase.append(message)


print_without_duplicates("HELLO")
print_without_duplicates("HELLO")
print_without_duplicates("hello")
print_without_duplicates("hello")
print_without_duplicates("Hello hello hello")
print_without_duplicates("HELLO")
print_without_duplicates("HELLO")