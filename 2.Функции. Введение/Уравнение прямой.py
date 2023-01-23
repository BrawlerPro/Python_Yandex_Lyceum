def equation(a, b):
    point1 = a.split(";")
    point2 = b.split(";")
    x1 = float(point1[0])
    y1 = float(point1[1])
    x2 = float(point2[0])
    y2 = float(point2[1])

    if y1 != y2 and x1 != x2:
        k = (y1 - y2) / (x1 - x2)
        b = y2 - k * x2
        print(str(k) + " " + str(b))
    else:
        if x1 == x2:
            print(x1)
        elif y1 == y2:
            print(y1)
