import sys

input = sys.stdin.readline

N = int(input())

data = [input().rstrip() for _ in range(N)]
file_length = len(data[0])

for idx in range(file_length):
    base = data[0][idx]
    is_same = True
    for file in data[1:]:
        if base != file[idx]:
            is_same = False
            break
    print(base if is_same else '?', end='')