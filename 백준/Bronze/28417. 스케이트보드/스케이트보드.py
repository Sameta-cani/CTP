import sys

input = sys.stdin.readline

max_score = -float('inf')
for _ in range(int(input())):
    scores = list(map(int, input().split()))
    res = max(scores[:2]) + sum(sorted(scores[2:])[-2:])
    max_score = max(max_score, res)
    
print(max_score)