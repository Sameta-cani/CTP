import sys

input = sys.stdin.readline

total = sum([int(input()) for _ in range(4)])

print(total // 60, total % 60)