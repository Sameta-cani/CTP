import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N-1, -1, -1):
    print(' ' * i + '*' * (N - i))