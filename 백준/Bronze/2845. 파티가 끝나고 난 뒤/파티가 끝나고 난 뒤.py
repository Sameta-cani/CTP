import sys

L, P = map(int, input().split())
ans = L * P

array = list(map(int, input().split()))

for val in array:
    print(val - ans, end=' ')