def hello(name):
    global query
    b = 0
    for p, i in enumerate(query):
        if i is None:
            print(f"Здравствуйте, {name}! Подойдите к окошку номер {p + 1}")
            query[p] = name
            return
    print(f"Простите, {name}. Все окна заняты")
    return


def good_bye(name):
    global query
    for p, i in enumerate(query):
        if name == i:
            print(f"До свидания, не болейте, {name}")
            query[p] = None
            return
    print(f"Простите, {name}, дождитесь своей очереди")


def search_card(name):
    for i in query:
        if i == name:
            for index, surename in enumerate(base):
                if surename == name:
                    print(f"Ваша карта с номером {index + 1} найдена")
                    return
            print("Ваша карта не найдена")
            return
    print(f"Простите, {name}, дождитесь своей очереди")
    return
