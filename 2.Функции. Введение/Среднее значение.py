def print_average(arr):
    mid = 0
    if len(arr) == 0:
        print(0)
    else:
        for elem in arr:
            mid += int(elem)
        mid = mid / len(arr)
        print(mid)
