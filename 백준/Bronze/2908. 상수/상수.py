import sys

A, B = sys.stdin.readline().rstrip().split()

A, B = int(A[::-1]), int(B[::-1])

print(max(A, B))