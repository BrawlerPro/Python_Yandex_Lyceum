template = {'B': 1,
            'KB': 1024,
            'MB': 1024 ** 2,
            'GB': 1024 ** 3
            }


def to_bytes(value: int, unit: str):
    return value * template[unit]


def in_largest_units(values: int):
    for index, value in reversed(template.items()):
        result = round(values / value)
        if result > 1:
            return f'{result} {index}'


print(f'{to_bytes(584, "B")} B')
print(in_largest_units(550823800))
