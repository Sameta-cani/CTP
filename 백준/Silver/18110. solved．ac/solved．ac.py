import sys
input = sys.stdin.readline

def roundup(n):
    if (n - int(n)) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

n = int(input())
if n == 0:
    print(0)
else:
    diffs = sorted([int(input()) for _ in range(n)])
    bound = roundup((n * 15) / 100)

    print(roundup(sum(diffs[bound:n-bound]) / (n - bound * 2)))