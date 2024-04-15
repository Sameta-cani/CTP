import sys

input = sys.stdin.readline

data = input()

count = 0
prev = data[0]
for digit in data[1:]:
    if prev != digit:
        count += 1
    prev = digit

print(count // 2)