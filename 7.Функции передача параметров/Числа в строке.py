def from_string_to_list(string, container):
    string2 = []
    string = string.split()
    for elem in string:
        string2.append(int(elem))
    container += string2
    a = container
