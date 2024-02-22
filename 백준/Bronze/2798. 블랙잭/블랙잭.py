from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_sum = 0
for comb in combinations(cards, 3):
    temp_sum = sum(comb)
    if temp_sum <= M:
        max_sum = max(max_sum, temp_sum)

print(max_sum)