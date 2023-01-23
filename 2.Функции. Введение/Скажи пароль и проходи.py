def ask_password():
    word = 'password'
    for i in range(3):
        wrd = input()
        if wrd == word:
            print('Пароль принят')
            break
        elif i == 2:
            print('В доступе отказано')
            break
