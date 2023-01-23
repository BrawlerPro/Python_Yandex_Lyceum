import json

banka = []
numbers = 0
with open('input.txt', 'r') as file:
    data = (file.readlines())
for linees in range(len(data) - 1):
    data[linees] = data[linees][:-1]
for linees in range(len(data)):
    life = True
    sl = ''
    for k in range(len(banka)):
        if data[linees][0] in banka[k]:
            life = False
            sl = k
    if life:
        banka.append([data[linees][0], 1])
        numbers += 1
    else:
        banka[sl][1] += 1
        numbers += 1
    if not banka:
        banka.append([data[linees][0], 1])
        numbers += 1

edata = {banka[i][0]: (banka[i][1] / numbers) * 100 for i in range(len(banka))}
with open('output.json', 'w') as file:
    json.dump(edata, file)
