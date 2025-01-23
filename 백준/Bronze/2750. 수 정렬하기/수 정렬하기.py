import sys

input = sys.stdin.readline

data = sorted([int(input()) for _ in range(int(input()))])

print('\n'.join(map(str, data)))