import sys

X = int(sys.stdin.readline().rstrip())
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    price = a * b
    X -= price

if not X:
    print('Yes')
else:
    print('No')