import sys

N = int(sys.stdin.readline().rstrip())
A = set(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
B = list(map(int, sys.stdin.readline().rstrip().split()))

for card in B:
    if card in A:
        print(1, end=' ')
    else:
        print(0, end=' ')