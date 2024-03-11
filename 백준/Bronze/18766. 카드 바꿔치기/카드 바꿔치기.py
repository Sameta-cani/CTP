from collections import Counter

T = int(input())

for _ in range(T):
    N = int(input())

    prev_game = Counter(list(input().split()))
    next_game = Counter(list(input().split()))

    if prev_game == next_game:
        print('NOT CHEATER')
    else:
        print('CHEATER')