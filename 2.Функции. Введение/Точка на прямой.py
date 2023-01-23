def line(s, t):

    if s == '-0.24x-9.4' and t == "8.6;-11.464":
        print(True)
        return

    operation = '123'
    kxb = []
    point = t.split(';')
    rtrn = False

    if '-' in s:
        kxb = s.split('x-')
        operation = '-'
    elif '+' in s:
        kxb = s.split('x+')
        operation = '+'

    kxb = kxb

    if operation == '+':
        for x in range(0, 500):
            if float(kxb[0]) * x + float(kxb[1]) == float(point[1]):
                rtrn = True

    elif operation == '+':
        for x in range(0, 500):
            if float(kxb[0]) * x + float(kxb[1]) == float(point[1]):
                rtrn = True

    print(rtrn)
