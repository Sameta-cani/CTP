import sys

N = int(sys.stdin.readline().rstrip())

count = 1

while N > 1 + 3 * count * (count - 1):
    count += 1

print(count)