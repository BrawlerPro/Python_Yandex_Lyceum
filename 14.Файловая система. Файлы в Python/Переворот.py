def revers():
    with open('input.dat', 'rb') as f:
        data = (f.read())
        revdata = (data[::-1])
        with open('output.dat', 'wb') as p:
            str(p.write(revdata))

