A, B = map(int, input().split())
C, D = map(int, input().split())

cond1 = A + D
cond2 = B + C

print(min(cond1, cond2))