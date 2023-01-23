import csv

with open('alpha_oriona.csv', 'r', encoding='utf-8') as file:
    result = []
    data = csv.reader(file, delimiter=';', quotechar='"')
    head = next(data)
    data = list(data)
    maxlu = int(data[0][2])
    maxk = 0
    k = 0
    maxdate, maxtime = data[0][0], data[0][1]
    history = 0
    data.pop(0)
    for index, obj in enumerate(data):
        if maxlu >= int(obj[2]):
            maxlu = int(obj[2])
            k += 1

        else:

            if k > maxk:
                maxk = k
                k = 1
                if index + 1 != len(data):
                    maxdate, maxtime = obj[0], obj[1]

            maxlu = int(obj[2])


with open('result.txt', "w", encoding="utf-8", newline='') as csvfile:
    csvfile.write(str(maxk)) + csvfile.write('\n')
    csvfile.write(maxdate) + csvfile.write(' ') + csvfile.write(maxtime)
