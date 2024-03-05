import sys

N = int(input())

scores = []

for _ in range(N):
    array = list(map(int, sys.stdin.readline().rstrip().split()))
    score = max(array[:2]) + sum(sorted(array[2:])[-2:])
    scores.append(score)

print(max(scores))