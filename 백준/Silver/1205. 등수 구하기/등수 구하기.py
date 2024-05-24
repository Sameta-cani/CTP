from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

N, new_score, P = map(int, input().split())
scores = sorted(list(map(int, input().split())))

if N - bisect_left(scores, new_score) == P:
    print(-1)
else:
    print(N - bisect_right(scores, new_score) + 1)