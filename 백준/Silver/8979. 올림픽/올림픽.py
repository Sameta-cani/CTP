import sys

input = sys.stdin.readline

N, K = map(int, input().split())
array = []
target = []

for _ in range(N):
    data = list(map(int, input().split()))
    if data[0] == K:
        target = data[1:]
    array.append(data)

array.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

for idx, item in enumerate(array, start=1):
    if item[1:] == target:
        print(idx)
        break