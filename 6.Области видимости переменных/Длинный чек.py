all_items = []
number = [1]


def add_item(item_name, item_cost):
    all_items.append(item_name)
    all_items.append(item_cost)


def print_receipt():
    if len(all_items) != 0:
        sum = 0

        print('Чек ' + str(number[0]) + '. Всего предметов: ' + str(len(all_items) // 2))
        for i in range(0, len(all_items), 2):
            print(all_items[i], '-', all_items[i + 1])

        for i in range(1, len(all_items), 2):
            sum += all_items[i]

        print('Итого:', sum)
        print('-----')
        all_items.clear()
        number[0] = number[0] + 1
