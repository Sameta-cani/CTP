import sys

input = sys.stdin.readline

data = sorted([int(input()) for _ in range(5)])

print(sum(data) // 5)
print(data[2])