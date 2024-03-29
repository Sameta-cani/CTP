import sys
input = sys.stdin.readline

N = int(input())

result = sum([int(input()) for _ in range(N)])

print(result - (N - 1))