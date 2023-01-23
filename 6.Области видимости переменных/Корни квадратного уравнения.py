def discriminant(a, b, c):
    d = (b * b) - (4 * a * c)
    return d


def larger_root(p, q):
    a = 1
    b = p
    c = q
    x = []

    d = discriminant(a, b, c)

    x.append((-b - pow(d, 0.5)) / (2 * a))
    x.append((-b + pow(d, 0.5)) / (2 * a))
    return max(x)


def smaller_root(p, q):
    a = 1
    b = p
    c = q
    x = []

    d = discriminant(a, b, c)

    x.append((-b + pow(d, 0.5)) / (2 * a))
    x.append((-b - pow(d, 0.5)) / (2 * a))
    return min(x)


def main():
    p = float(input())
    q = float(input())
    print(discriminant(1, p, q))
    print(str(smaller_root(p, q)) + ' ' + str(larger_root(p, q)))
