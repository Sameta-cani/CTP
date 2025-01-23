import sys

input = sys.stdin.readline

data = [input().strip().split() for _ in range(int(input()))]

data.sort(key=lambda x: (-int(x[1]), x[0]))

print(data[0][0])