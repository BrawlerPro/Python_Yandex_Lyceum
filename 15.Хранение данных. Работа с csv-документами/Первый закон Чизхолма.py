import csv

opdat = []
with open('salary.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    headers = next(data)
    with open('out_file.csv', "w", encoding="utf8", newline='') as csvfile:
        for offers in data:
            opdat.append(offers)
        fedokrug = input()
        goda = input()
        goda = goda.split(' ')
        nzgd, nzgd2 = 0, 0
        numbers = []
        nokrug = []
        schet = 0
        zb = 0
        zb4 = 0
        for stolb in range(len(headers)):
            if goda[0] == headers[stolb]:
                nzgd = stolb
            if goda[1] == headers[stolb]:
                nzgd2 = stolb
        for y in range(len(opdat)):
            if fedokrug == opdat[y][1]:
                numbers.append([opdat[y][nzgd], opdat[y][nzgd2]])
                nokrug.append(opdat[y][0])
        # numbers = [['24444', '25968'],
        #            ['20092', '21458'],
        #            ['22807', '24239']]

        for index, y in enumerate(numbers):
            for x in range(len(y)):
                if y[x] == numbers[index][0]:
                    zb = int(y[x])
                    zb4 = int(y[x]) / 100 * 4
                else:
                    if int(y[x]) < zb + zb4:
                        if schet == 0:
                            csvfile.write('Субъект') + csvfile.write(';') + csvfile.write(str(goda[0])) + csvfile.write(
                                str(';'))
                            csvfile.write(str(goda[1])) + csvfile.write('\n')
                            csvfile.write(nokrug[index]) + csvfile.write(';') + csvfile.write(str(zb))
                            csvfile.write(';') + csvfile.write(str(y[x])) + csvfile.write('\n')
                        else:
                            csvfile.write(nokrug[index]) + csvfile.write(';') + csvfile.write(str(zb))
                            csvfile.write(';') + csvfile.write(str(y[x])) + csvfile.write('\n')
                        schet += 1