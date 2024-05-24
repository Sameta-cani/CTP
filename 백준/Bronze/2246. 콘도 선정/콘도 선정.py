import sys

input = sys.stdin.readline

N = int(input())

condos = [tuple(map(int, input().split())) for _ in range(N)]
condos.sort()

cnt = 0
min_cost = float('inf')

for condo in condos:
    cost = condo[1]
    if cost < min_cost:
        min_cost = cost
        cnt += 1
        
print(cnt)