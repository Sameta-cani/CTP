import sys

N, M = map(int, sys.stdin.readline().rstrip().split())

A = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]

for i in range(N):
    data = [int(x) for x in input().split()]
    for j in range(M):
        A[i][j] += data[j]

for row in A:
    print(*row)