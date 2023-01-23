with open('in_file.txt', 'r', encoding='utf-8') as file:
    num = file.readline()
    data = file.read()
    gdata = []
    nuznoff = []
    sumoffers = 0
    for pril in data.split('\n'):
        off = pril.split('\r')
        gdata.append(*off)
    for offers in gdata:
        sumoffers += len(offers)
    lenoffers = sumoffers // len(gdata)
    for offers in gdata:
        if len(offers) == lenoffers:
            nuznoff.append(offers)
        if len(offers) + int(num) == lenoffers:
            nuznoff.append(offers)
    with open('out_file.txt', 'w', encoding='utf-8') as pfile:
        pfile.write(str(lenoffers)) + pfile.write('\n')
        for sl in nuznoff:
            pfile.write(sl) + pfile.write('\n')
