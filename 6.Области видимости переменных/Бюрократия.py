name = ''
date = ''


def setup_profile(n, d):
    global name
    name = n
    global date
    date = d


def print_application_for_leave():
    print('Заявление на отпуск в период ' + date + '. ' + name)


def print_holiday_money_claim(money):
    print('Прошу выплатить ' + money + ' отпускных денег. ' + name)


def print_attorney_letter(name2):
    print('На время отпуска в период ' + date + ' моим заместителем назначается ' + name2 + '. ' + name)
