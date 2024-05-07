import sys

input = sys.stdin.readline

N = int(input())

data = []
for _ in range(N):
   data += list(map(int, input().split()))
   data = sorted(data, reverse=True)[:N]

print(data[N - 1])