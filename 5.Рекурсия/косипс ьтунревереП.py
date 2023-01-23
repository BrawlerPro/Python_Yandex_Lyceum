def recursive_reverse(some_list):
    if not some_list:
        return []
    else:
        return [some_list.pop()] + recursive_reverse(some_list)

