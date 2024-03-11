import sys

N = int(sys.stdin.readline().rstrip())
array = sorted(set(map(int, sys.stdin.readline().rstrip().split())))

print(*array)