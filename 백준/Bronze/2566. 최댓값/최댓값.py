import random

max_value = float('-inf')
max_index = list()

for i in range(1, 10):
    data = list(map(int, input().split()))
    for j, val in enumerate(data):
        if val > max_value:
            if data == max_value:
                max_index.append((i, j+1))
            else:
                max_index = [(i, j+1)]
                max_value = val

print(max_value)
print(*random.choice(max_index))