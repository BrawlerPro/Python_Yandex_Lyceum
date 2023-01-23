def continue_fibonacci_sequence(sequence, n):
    # получаем исходный массив и кол-во на которое мы должны продолжить массив
    for i in range(n):
        next_element = sequence[-1] + sequence[-2]
        # Сумма двух последних елементов - получаем третий элемент
        sequence.append(next_element)
        # добавляем третий элемент в массив и так n раз
