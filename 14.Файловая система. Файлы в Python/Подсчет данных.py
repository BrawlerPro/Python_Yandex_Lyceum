def goal():
    global pol
    global otris
    global nul
    if pol == 0:
        return '-1', str(otris), '0', str(nul)
    if otris == 0 and nul == 0:
        return '1', str(pol)
    if pol == 0 and otris == 0:
        return '0', str(nul)
    if pol == 0 and nul == 0:
        return '-1', str(otris)
    if otris == 0:
        return '1', str(pol), '0', str(nul)
    if nul == 0:
        return '1', str(pol), '-1', str(otris)
    else:
        return '1', str(pol), '-1', str(otris), '0', str(nul)


with open('input.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    data = data.split()
    pol = 0
    otris = 0
    nul = 0
    kolvo = len(data)
    if kolvo == 0:
        with open('output.txt', 'w', encoding='utf-8') as outfile:
            outfile.write(str(kolvo)) + outfile.write('\n')
    else:
        for num in data:
            if int(num) > 0:
                pol += 1
            if int(num) < 0:
                otris += 1
            if int(num) == 0:
                nul += 1
        sort = goal()
        with open('output.txt', 'w', encoding='utf-8') as outfile:
            outfile.write(str(kolvo)) + outfile.write('\n')
            for sl in sort:
                outfile.write(sl) + outfile.write(' ')
