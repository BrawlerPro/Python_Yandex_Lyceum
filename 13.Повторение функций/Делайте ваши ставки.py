unbeted_horses = []


def do_bet(horse_num, bet):
    if horse_num not in unbeted_horses and bet > 0 and horse_num <= 10 and horse_num > 0:
        print('Ваша ставка в размере ' + str(bet) + ' на лошадь ' + str(horse_num) + ' принята')
        unbeted_horses.append(horse_num)
    else:
        print('Что-то пошло не так, попробуйте еще раз')

