kaspersky = []


def vaccine_effect(array, value):
    for elem in array:
        if elem[1] >= value:
            kaspersky.append(elem)
        else:
            array.remove(elem)
    for elem in array:
        if elem[1] >= value:
            kaspersky.append(elem)
        else:
            vaccine_effect(array, value)

