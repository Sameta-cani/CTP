import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
baskets = [0] * N

for _ in range(M):
    i, j, k = map(int, sys.stdin.readline().rstrip().split())
    baskets[i-1:j] = [k] * (j - i + 1)

print(*baskets)