import sys

N, K = map(int, sys.stdin.readline().rstrip().split())

print(sorted(list(map(int, sys.stdin.readline().rstrip().split())))[K-1])