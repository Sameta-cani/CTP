import sys

N = int(input())

scores = []
for _ in range(N):
    scores.append(tuple(sys.stdin.readline().rstrip().split()))

scores.sort()
scores.sort(key=lambda x: int(x[1]), reverse=True)

sys.stdout.write(scores[0][0])