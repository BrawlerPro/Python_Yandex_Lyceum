phrase = input().split()
lst = []

for elem in phrase:
    lst.append(elem.count('а') + elem.count('у'))

bad = False
for i in lst:
    if lst[0] != i:
        bad = True

if bad:
    print('Пам парам')
else:
    print('Парам пам-пам')

if