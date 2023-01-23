x = int(input())
y = int(input())
z = int(input())
a = 0
for i in range(x):
    if (i < x) and (not(i < y)) or (i <= z):
        a += 1

print(a)
