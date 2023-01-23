import json

russl = []
with open('russian_words.txt', 'r') as file:
    data = (file.readlines())
for num in range(len(data) - 1):
    data[num] = data[num][:-1]
    russl.append(data[num][0])
russl.append(data[-1][0])
redson = {russl[r]: [] for r in range(len(data))}
for num in range(len(data)):
    redson[russl[num]].append(data[num])
with open('russian_words.json', 'w') as pfile:
    json.dump(redson, pfile, ensure_ascii=False)
