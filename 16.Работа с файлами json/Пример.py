def recursive_reverse(slovo):
    if not slovo:
        return []
    return [slovo.pop()] + recursive_reverse(slovo)


reversed_list = recursive_reverse([1, 2, 3])
print(*reversed_list)