import sys

input = sys.stdin.readline

N = int(input())
count = 0

is_empty = [True] * 101

data = list(map(int, input().split()))

for value in data:
    if is_empty[value]:
        is_empty[value] = False
    else:
        count += 1

print(count)