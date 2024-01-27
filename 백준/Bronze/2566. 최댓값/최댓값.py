import random
import sys

max_value = float('-inf')
max_positions = list()

for i in range(1, 10):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    for j, val in enumerate(data):
        if val > max_value:
            max_positions = [(i, j+1)]
            max_value = val
        elif val == max_value:
            max_positions.append((i, j+1))

print(max_value)
print(*random.choice(max_positions))