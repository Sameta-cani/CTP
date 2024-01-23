import sys

N = int(sys.stdin.readline().rstrip())
data = [int(x) for x in sys.stdin.readline().rstrip().split()]
v = int(sys.stdin.readline().rstrip())

print(data.count(v))