from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

array = []

for _ in range(N):
    data = list(map(int, input().split()))
    if data[0] == K:
        target = data[1:]
    array.append(data)

array = sorted(array, key=lambda x: (x[1], x[2], x[3]), reverse=True)
array = deque(array)

count = 0
while array:
    current = array.popleft()
    count += 1
    if current[1:] == target:
        break

print(count)