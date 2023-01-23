def big_data(*edata, key=None):
    edata = [*edata]
    for index, mesto in enumerate(edata):
        name, _ = mesto[-1].split('@')
        date = mesto[1].split('-')
        edata[index] = mesto + (''.join([name.capitalize(), date[0][0], date[1][-1], date[2][-1]]),)
    edata = sorted(edata, key=key)
    return edata


data = [(123, '14-05-2020', 'username@gmail.com'),
        (21, '12-06-2020', 'ara@gmail.com'),
        (4123, '02-09-2020', 'unknown@yandex.ru'),
        (1253, '17-05-2020', 'qwerty@mail.ru')]
func = lambda x: x[-1]
print(*big_data(*data, key=func), sep='\n')
