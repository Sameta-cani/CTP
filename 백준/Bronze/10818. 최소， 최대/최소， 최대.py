import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

print(min(data), max(data))