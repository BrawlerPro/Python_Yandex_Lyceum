import sys
import json

data = []
banka = []

for strocka in sys.stdin:
    data.append(strocka[:-1])


for offers in data:
    num = offers
    schet = 0
    while len(str(num)) > 1:
        schet += 1
        rnumber = 1
        for number in str(num):
            rnumber *= int(number)
        num = rnumber
    if len(offers) == 1:
        banka.append(1)
    else:
        banka.append(schet)


edata = {banka[lol]: [] for lol in range(len(banka))}
for offers in range(len(data)):
    edata[banka[offers]].append(data[offers])
with open('numbers_age.json', 'w') as file:
    json.dump(edata, file)
