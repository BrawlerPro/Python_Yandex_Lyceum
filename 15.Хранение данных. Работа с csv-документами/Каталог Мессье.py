import csv
with open('messier.txt', 'r', encoding='utf-8') as file:
    data = csv.reader(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    headers = next(data)
    with open('messier.csv', "w", encoding="utf8", newline='') as csvfile:
        for index, sl in enumerate(headers):
            if index == len(headers) - 1:
                csvfile.write(sl) + csvfile.write('\n')
            else:
                csvfile.write(sl) + csvfile.write(';')
        for offers in data:
            for index, sl in enumerate(offers):
                if index == len(offers) - 1:
                    csvfile.write(sl) + csvfile.write('\n')
                else:
                    csvfile.write(sl) + csvfile.write(';')