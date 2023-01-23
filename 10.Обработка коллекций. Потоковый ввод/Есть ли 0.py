import sys
data = ''
for txt in sys.stdin:
    data += ' ' + str(txt.rstrip('\n'))

print('0' in data.split())
if