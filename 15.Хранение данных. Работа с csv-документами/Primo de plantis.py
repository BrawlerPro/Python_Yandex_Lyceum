import csv
import sys

data = []
for strocka in sys.stdin:
    data.append(strocka)

with open('plantis.csv', "w", encoding="utf8") as csvfile:
    data = csv.reader(data, delimiter='\t')
    headers = "nomen;definitio;pluma;Russian nomen;familia;Russian nomen familia\n"
    csvfile.write(headers)
    for offers in data:
        for index, sl in enumerate(offers):
            if index == len(offers) - 1:
                csvfile.write(sl) + csvfile.write('\n')
            else:
                csvfile.write(sl) + csvfile.write(';')