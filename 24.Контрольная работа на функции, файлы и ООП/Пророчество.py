import csv
import json

with open(' predict.csv', 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    headers = next(data)
    data = list(data)
    loki = []
    for index, obj in enumerate(data):
        if len(data[index][0]) <= int(data[index][2]):
            u = {
                'predicti': data[index][0],
                'years ago': data[index][1]
            }
            loki.append(u)
with open('validation.json', 'w') as file:
    json.dump(loki, file)