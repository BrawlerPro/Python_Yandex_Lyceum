def recursive_len(some_list):
    if len(some_list) == 0:
        return 0
    else:
        return recursive_len(some_list[1:]) + 1
