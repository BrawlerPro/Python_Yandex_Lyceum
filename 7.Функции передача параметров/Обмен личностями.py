def swap(first, second):
    list3 = []
    for elem in second:
        list3.append(elem)

    second.clear()
    for elem in first:
        second.append(elem)

    first.clear()
    for elem in list3:
        first.append(elem)


