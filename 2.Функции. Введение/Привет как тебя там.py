def who_are_you_and_hello():
    name = 'fgfg  we'
    while True:
        if name == "".join(filter(str.isalpha, name)) and\
                name == name.title() and\
                len(name.split()) == 1:
            print('Привет, ' + name + '!')
            break
        name = input()
