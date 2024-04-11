from collections import defaultdict
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    W = input()
    K = int(input())
    char_indices = defaultdict(list)

    for i, char in enumerate(W):
        char_indices[char].append(i)

    min_gap, max_gap = sys.maxsize, -sys.maxsize

    for indices in char_indices.values():
        if len(indices) >= K:
            for i in range(len(indices) - K + 1):
                start_index = indices[i]
                end_index = indices[i + K - 1]
                gap = end_index - start_index + 1
                min_gap = min(min_gap, gap)
                max_gap = max(max_gap, gap)

    if min_gap == sys.maxsize:
        print(-1)
    else:
        print(min_gap, max_gap)