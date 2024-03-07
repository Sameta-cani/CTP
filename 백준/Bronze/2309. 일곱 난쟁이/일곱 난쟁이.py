from itertools import combinations
import random

array = [int(input()) for _ in range(9)]

events = [event for event in combinations(array, 7) if sum(event) == 100]

print(*sorted(random.sample(events, k=1)[0]), sep='\n')