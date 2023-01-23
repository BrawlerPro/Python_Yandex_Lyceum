import csv


def resort(x):
    while True:
        if '' in x:
            for off in x:
                if off == '':
                    x.remove(off)
        else:
            break
    return x


def messier_search(param):
    with open('messier.csv', 'r', encoding='utf-8') as file:
        result = []
        data = csv.DictReader(file, delimiter=';', quotechar='"')
        data = list(sorted(map(lambda x: str(x[param]), data)))
        for index, sl in enumerate(data):
            if sl not in result:
                result.append(sl)
        return resort(result)
