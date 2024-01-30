import sys

data = [sys.stdin.readline().rstrip() for _ in range(5)]
max_len = max(len(line) for line in data)

for i in range(max_len):
    for j in range(5):
        if i < len(data[j]):
            print(data[j][i], end='')