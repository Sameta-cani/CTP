from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

res = 0
for iter in combinations(cards, 3):
    if sum(iter) <= M:
        res = max(res, sum(iter))
        
print(res)