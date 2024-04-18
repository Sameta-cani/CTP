import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

max_count = 0
for i in range(N):
    count = 0
    if max_count < N - (i + 1):
        for j in range(i + 1, N):
            if array[i] > array[j]:
                count += 1
            else:
                break
        max_count = max(max_count, count)

print(max_count)