def rec_linear_sum(some_list):
    if not some_list:
        return 0

    if len(some_list) == 1:
        return some_list[0]
    else:
        return some_list.pop() + rec_linear_sum(some_list)
