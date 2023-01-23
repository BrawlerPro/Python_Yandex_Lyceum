import json


def numforsort(jsondata):
    color = len(jsondata['colors'])
    radius = jsondata['radius']
    vektor_udaleniya = (jsondata['x'] ** 2 + jsondata['y'] ** 2) ** 0.5
    idishnik = jsondata['id']
    return color, radius, vektor_udaleniya, idishnik


with open('input.json') as file:
    data = json.load(file)
    sortdata = reversed(sorted(data, key=numforsort))
    for i in sortdata:
        print(i["id"], end=' ')
