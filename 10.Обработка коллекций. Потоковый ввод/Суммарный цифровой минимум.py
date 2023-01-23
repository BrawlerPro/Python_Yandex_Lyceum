import sys


def main(num):
    output = 0
    for i in range(0, len(num) - 1):
        output += int(str(num)[i])
    return output


data = []

for line in sys.stdin:
    data.append(line.rstrip('\n'))

new_data = sorted(data, key=main, revers=True)
print(new_data[0])
