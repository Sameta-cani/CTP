import sys

N = int(sys.stdin.readline().rstrip())
data = [int(x) for x in sys.stdin.readline().rstrip().split()]

print(min(data), max(data))