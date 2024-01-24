import sys

N = int(sys.stdin.readline().rstrip())
scores = [int(x) for x in sys.stdin.readline().rstrip().split()]
M = max(scores)

adjusted_avg = sum(score / M * 100 for score in scores) / N

print(adjusted_avg)