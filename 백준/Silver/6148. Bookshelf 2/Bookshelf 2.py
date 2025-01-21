from itertools import combinations
import sys

input = sys.stdin.readline

N, B = map(int, input().split())
Hs = [int(input()) for _ in range(N)]

min_val = float("INF")
for idx in range(1, N + 1):
    lst = list(combinations(Hs, idx))
    for chance in lst:
        sum_val = sum(chance)
        if sum_val >= B:
            min_val = min(min_val, sum_val)
            
print(min_val - B)