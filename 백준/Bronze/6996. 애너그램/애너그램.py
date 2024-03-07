from collections import Counter

T = int(input())

for _ in range(T):
    a, b = input().split()

    a_freq = Counter(a)
    b_freq = Counter(b)

    if a_freq == b_freq:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')