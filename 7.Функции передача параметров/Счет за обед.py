daily_food = [0, 150, 150]


def count_food(days):
    sum = 0
    for i in days:
        sum += daily_food[i - 1]
    return sum


