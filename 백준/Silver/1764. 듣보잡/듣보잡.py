from collections import Counter
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cond = Counter([input().strip() for _ in range(N + M)])

res = sorted([name for name, cnt in cond.items() if cnt == 2])
print(len(res))
print(*res, sep='\n')