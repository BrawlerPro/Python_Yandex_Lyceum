name = [']123321123321']


def polite_input(question):
    if name[0] == '123321123321':
        print('Как вас зовут?')
        name[0] = input()
    print(name[0] + ', ' + question)
    return input()
