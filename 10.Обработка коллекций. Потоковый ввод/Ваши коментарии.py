import sys
text = []
text_copy = []
for line in sys.stdin:
    text.append(line.rstrip('\n'))

for elem in text:
    data = elem.split()
    text_copy.append(' '.join(data))

count = list(filter(lambda x: x[0:1] == '#', text_copy))

print(len(count))
