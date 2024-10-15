import sys
input = sys.stdin.readline

data = [int(input()) for _ in range(9)]

print(max(data), data.index(max(data)) + 1)