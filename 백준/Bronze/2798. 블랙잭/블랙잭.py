from itertools import combinations
from bisect import bisect

N, M = map(int, input().split())
cards = list(map(int, input().split()))

comb = list(map(sum, list(combinations(cards, 3))))
comb.sort()

print(comb[bisect(comb, M)-1])