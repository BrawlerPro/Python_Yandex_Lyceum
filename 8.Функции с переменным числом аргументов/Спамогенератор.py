def spam_generation(*args):

    if len(args) == 4:
        name = args[0]
        place = args[1]
        date = args[2]
        email = args[3]
    elif len(args) == 3:
        name = args[0]
        place = 'Москва'
        date = args[1]
        email = args[2]

    spam_text = """To: {email}
Здравствуйте, {name}!
Были бы рады видеть вас на встрече начинающих программистов в {place},
которая пройдет {date}.""".format(email=email, name=name, date=date, place=place)

    return spam_text
