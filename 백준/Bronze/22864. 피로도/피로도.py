import sys

input = sys.stdin.readline

A, B, C, M = map(int, input().split())

res = 0
Fatigue = 0
for _ in range(24):
    if Fatigue + A <= M:
        res += B
        Fatigue += A
    else:
        Fatigue -= C
        Fatigue = max(Fatigue, 0)
    
print(res)