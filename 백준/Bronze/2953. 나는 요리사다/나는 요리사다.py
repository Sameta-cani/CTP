import sys

input = sys.stdin.readline

scores = [list(map(int, input().split())) for _ in range(5)]

max_value = -int(1e9)
max_index = 0

for idx, score in enumerate(scores, start=1):
    if max_value < sum(score):
        max_value = sum(score)
        max_index = idx

print(max_index, max_value)