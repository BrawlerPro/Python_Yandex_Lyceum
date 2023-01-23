jokes = set()


def print_only_new(message):
    if message not in jokes:
        jokes.add(message)
        print(message)
