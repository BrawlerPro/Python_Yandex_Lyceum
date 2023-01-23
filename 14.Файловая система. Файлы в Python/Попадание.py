import sys
schetchik = 0
pusta = []
popdaniya = []
for i in sys.stdin:
    schetchik += 1
    broski = int(i.strip())
    if int(broski) == schetchik:
        popdaniya.append(int(broski))
if popdaniya == pusta:
    popdaniya.append(0)
print(popdaniya)
with open('output.txt', 'w', encoding='utf-8') as file:
    for num in popdaniya:
        file.write(str(num)) + file.write(' ')