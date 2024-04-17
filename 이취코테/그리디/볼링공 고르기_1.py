import sys

input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))

count = 0

for i in range(N):
    for j in range(i + 1, N):
        if array[i] != array[j]:
            count += 1

print(count)