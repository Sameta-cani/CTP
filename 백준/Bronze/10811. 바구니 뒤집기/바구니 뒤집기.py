import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
positions = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    positions[i-1:j] = positions[i-1:j][::-1]

print(*positions)