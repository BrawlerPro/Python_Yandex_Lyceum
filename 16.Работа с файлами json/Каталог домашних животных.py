import csv
import json

data = []
banka = []
with open('catalog.csv', encoding="utf8") as csvfile:
    inpdat = csv.reader(csvfile, delimiter=';', quotechar='"')
    for line in inpdat:
        banka.append(line)
banka = banka[1:]
for i in range(len(banka)):
    if not data:
        data.append([banka[i][0], [[banka[i][1], [banka[i][2:]]]]])
    else:
        choose = False
        sche = 0
        for mat in range(len(data)):
            if banka[i][0] == data[mat][0]:
                choose = True
                sche = mat
        if not choose:
            data.append([banka[i][0], [[banka[i][1], [banka[i][2:]]]]])
        else:
            choose = False
            ch = 0
            for k in range(len(data[sche][1])):
                if banka[i][1] == data[sche][1][k][0]:
                    choose = True
                    ch = k
            if not choose:
                data[sche][1].append([banka[i][1], [banka[i][2:]]])
            else:
                data[sche][1][ch][1].append(banka[i][2:])
opdat = {"type": {data[i][0]: {"breed": {data[i][1][num][0]: [
    {"name": data[i][1][num][1][k][0],
     "age": data[i][1][num][1][k][1],
     "gender": data[i][1][num][1][k][2],
     "owner": data[i][1][num][1][k][3],
     "phone": data[i][1][num][1][k][4]
     }
    for k in range(len(data[i][1][num][1]))]
    for num in range(len(data[i][1]))}
} for i in range(len(data))
}
}
with open('pets.json', 'w') as file:
    json.dump(opdat, file)
