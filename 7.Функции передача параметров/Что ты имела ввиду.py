numbers = [2, 5, 7, 7, 8, 4, 1, 6]
odd = []
even = []
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

    # программа делит числа на чётные и нечётные, но не выводит результат
    # также, odd и even явзяются одним списком, что стоит исправить
print('Чётные:', even)
print('Нечётные:', odd)