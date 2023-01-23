def matrix(n=-1, m=-1, a=-1):
    mtrx = []

    if n == -1 and m == -1:
        n, m, a = 1, 1, 0
        for i in range(n):
            row = []
            for k in range(m):
                row.append(a)
            mtrx.append(row)

    elif n != -1 and m == -1:
        m, a = 1, 0
        for i in range(n):
            row = []
            for k in range(n):
                row.append(a)
            mtrx.append(row)

    elif n != -1 and m != -1 and a == -1:
        a = 0
        for i in range(n):
            row = []
            for k in range(m):
                row.append(a)
            mtrx.append(row)

    elif n != -1 and m != -1 and a != -1:
        for i in range(n):
            row = []
            for k in range(m):
                row.append(a)
            mtrx.append(row)

    return mtrx
