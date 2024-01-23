import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
baskets = list(range(1, N+1))

for _ in range(M):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

print(*baskets)