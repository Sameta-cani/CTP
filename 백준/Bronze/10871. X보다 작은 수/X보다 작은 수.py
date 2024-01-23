import sys

N, X = map(int, sys.stdin.readline().rstrip().split())
data = [int(x) for x in sys.stdin.readline().rstrip().split()]


print(*[val for val in data if val < X])