num_of_classes = int(input())
data = []
for i in range(num_of_classes):
    class_ = []
    num_of_puple = int(input())
    for j in range(num_of_puple):
        info = input()
        class_.append(info[-1:])
    data.append(class_)

bool_data = []
for elem in data:
    print(elem)
    bool_data.append(any(x == '5' for x in elem))

if all(bool_data):
    print('ДА')
else:
    print('НЕТ')
