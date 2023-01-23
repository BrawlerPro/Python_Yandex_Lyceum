def str_to_nums(some_list):
    if type(some_list) is list:
        output = []
        for elem in some_list:
            output.append(int(elem))
        print(output)
        return output
    elif type(some_list) is str:
        nums = some_list.split('.')
        return list_to_nums(nums)


graph = []
points = input()
while len(points.split()) != 2:
    points = points.split()
    way = points[2]
    points = points[0] + '.' + points[1]
    graph.append(points)
    graph.append(way)
    points = input()

print(graph)
print(str_to_nums(graph[0]))

з
