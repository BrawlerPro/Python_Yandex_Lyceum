def roman():
    global three
    three = one + two

    def transrom(number):
        notraf = ''
        romanium = {1: 'IVX', 10: 'XLC', 100: 'CDM', 1000: 'M  '}
        for i in (1000, 100, 10, 1):
            if number // i != 0:
                rn, rnu, rnum = romanium[i]
                rnumf = (rn, rn * 2, rn * 3, rn + rnu, rnu, rnu + rn, rnu + 2 * rn, rnu + 3 * rn, rn + rnum)
                notraf += rnumf[number // i - 1]
                number = number - (number // i) * i
        return notraf

    print(f"{transrom(one)} + {transrom(two)} = {transrom(one + two)}")
one = 23
two = 34
roman()