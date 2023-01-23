my_str = 'Discworld'
my_str.startswith('Mad')  # False
my_str.startswith('Disc')  # True
my_str.startswith(('Disc', 'Mad'))  # True
p(my_str.startswith('world', 4, 9))  # True
