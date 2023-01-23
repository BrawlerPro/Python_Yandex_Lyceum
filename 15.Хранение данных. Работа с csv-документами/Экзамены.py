import csv
import sys


def numforsort(jsondata):
    name = jsondata[0]
    surename = jsondata[1]
    result1 = int(jsondata[2])
    reesult2 = int(jsondata[3])
    reesult3 = int(jsondata[4])
    sum = result1 + reesult2 + reesult3

    return [name, surename, str(result1), str(reesult2), str(reesult3), str(sum)]


num = input().split(' ')
data = []
for offers in sys.stdin:
    data.append(offers)
edat = []
sortedat = []
data = csv.reader(data, delimiter=' ', quotechar='"', quoting=csv.QUOTE_MINIMAL)
for index, sl in enumerate(data):
    if int(sl[2]) < int(num[1]) and int(sl[3]) < int(num[1]) and int(sl[4]) < int(num[1]):
        if int(sl[2]) + int(sl[3]) + int(sl[4]) > int(num[0]):
            sortedat.append(numforsort(sl))
    if int(sl[2]) >= int(num[1]) and int(sl[3]) >= int(num[1]) and int(sl[4]) >= int(num[1]):
        if int(sl[2]) + int(sl[3]) + int(sl[4]) >= int(num[0]):
            sortedat.append(numforsort(sl))
with open('exam.csv', "w", encoding="utf8", newline='') as csvfile:
    csvfile.write('Фамилия;имя;результат 1;результат 2;результат 3;сумма') + csvfile.write('\n')
    for off in sortedat:
        for dex, ls in enumerate(off):
            if dex == len(off) - 1:
                csvfile.write(str(ls)) + csvfile.write('\n')
            else:
                csvfile.write(str(ls)) + csvfile.write(';')
