def simple_map(transformation, values):
    result = []
    for elem in values:
        result.append(transformation(elem))
    return result
