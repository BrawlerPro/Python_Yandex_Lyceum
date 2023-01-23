import json
import sys

formula = {"complex": []}
data = []
proexample = []
for offers in sys.stdin:
    data.append((offers.strip()).split(' = ')[1])
for example in data:
    xex = example.split(' ')
    for i in xex[0:3]:
        proexample.append(i)
    if '+' in proexample:
        formula["complex"].append({
            "Re": float(proexample[0]),
            "Im": float(proexample[2])
        })
    if '-' in proexample:
        Re = float(proexample[0])
        Im = float(float(proexample[2]) + float(proexample[2]) * -2)
        formula["complex"].append({
            "Re": Re,
            "Im": Im
        })
    proexample = []

with open('output.json', 'w') as file:
    json.dump(formula, file)
