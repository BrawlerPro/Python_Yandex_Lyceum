def same_by(characteristic, objects):

    list = []

    for elem in objects:
        list.append(characteristic(elem))

    switch = False
    for i in range(len(list)):
        if list[0] != list[i]:
            switch = True

    if switch:
        return False
    else:
        return True
