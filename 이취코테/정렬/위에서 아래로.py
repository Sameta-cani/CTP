import sys

input = sys.stdin.readline

data = sorted([int(input()) for _ in range(int(input()))], reverse=True)

print(*data, sep=' ')