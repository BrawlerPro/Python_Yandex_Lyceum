def vaccine_filter(immunoglobulins, func):
    kaspersky = [*filter(func, immunoglobulins)]
    for x in immunoglobulins:
        if x in kaspersky:
            o = 1 + 1
        else:
            immunoglobulins.remove(x)
    for x in immunoglobulins:
        if x in kaspersky:
            o = 1 + 1
        else:
            vaccine_filter(immunoglobulins, func)


immunoglobulins = [('IgE', 2), ('IgA', 3),
                   ('IgG', 17), ('IgF', 4),
                   ('IgX', 21), ('IgZ', 5)]
vaccine_filter(immunoglobulins, lambda x: x[1] > 4)
print(*immunoglobulins, sep='\n')