import sys
input = sys.stdin.readline

res = 0
N = int(input())

data = [int(input()) for _ in range(N)]

for idx in range(N-1, 0, -1):
    res += (data[idx] - data[idx-1])**2

print(res)