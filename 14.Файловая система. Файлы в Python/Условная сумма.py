with open('data.txt', 'r', encoding='utf-8') as file:
    N = file.readline()
    delnum = []
    sumnum = 0
    numbers = file.readline()
    numbers = numbers.split()
    for number in numbers:
        for chis in range(int(N)):
            if chis // int(number) == chis / int(number) and chis not in delnum:
                delnum.append(chis)
    for num in delnum:
        sumnum += int(num)
    print(sumnum)