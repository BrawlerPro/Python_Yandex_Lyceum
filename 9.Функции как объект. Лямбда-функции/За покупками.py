[print(elem[1:]) if elem[0] == '*' else print(elem) for elem in
 list(filter(lambda x: x[0] != 'V' and x[0] != 'v', input().split('; ')))]