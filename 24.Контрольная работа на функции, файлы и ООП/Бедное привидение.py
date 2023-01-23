import sys
data = []
offers = []
kol = {}
for line in sys.stdin:
    data.append(line.split('\n'))
for i in range(len(data)):
    offers.append(data[i][0].split(' '))
for index, num in enumerate(offers):
    k = 0
    for number in num:
        if 5 < int(number) < 50:
            k += 1
    jo = index + 1
    kol.update({jo: k})
print(kol)
