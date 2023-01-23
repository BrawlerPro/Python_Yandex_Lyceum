with open('prices.txt', mode='r', encoding='utf-8') as f:
    ryad = f.read()

    result = 0
    for line in ryad.split("\n"):
        if line:
            sl, kolvo, thsena = line.split()
            result += float(kolvo) * float(thsena)

print(result)