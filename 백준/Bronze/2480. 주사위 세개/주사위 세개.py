import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())

unique_count = len(set([A, B, C]))

if unique_count == 1:
    print(10000 + A * 1000)
elif unique_count == 2:
    if A == B or A == C:
        print(1000 + A * 100)
    else:
        print(1000 + B * 100)
else:
    print(max(A, B, C) * 100)