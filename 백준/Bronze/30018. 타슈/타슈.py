import sys

input = sys.stdin.readline

N = int(input())
A_array = list(map(int, input().split()))
B_array = list(map(int, input().split()))

count = 0

for i in range(N):
    if A_array[i] < B_array[i]:
        count += B_array[i] - A_array[i]

print(count)