import sys
nums = []
for line in sys.stdin:
    nums.append(line.rstrip('\n'))

output = 0

if len(nums) == 0:
    print(-1)
else:
    for num in nums:
        output += int(num)

    print(output / len(nums))