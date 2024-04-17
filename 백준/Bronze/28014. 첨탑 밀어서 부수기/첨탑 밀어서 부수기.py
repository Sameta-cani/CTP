import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

count = 1
for index in range(N - 1):
    if array[index] <= array[index + 1]:
        count += 1

print(count)