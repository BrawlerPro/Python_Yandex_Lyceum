import csv

n = int(input())
with open('vps.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    headers = next(reader)
    for index, spisok in enumerate(reader):
        if int(spisok[-2]) >= n:
            print(spisok[0])