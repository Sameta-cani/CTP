A, B = map(int, input().split())
C = int(input())

total_m = A * 60 + B + C

h = (total_m // 60) % 24
m = (total_m % 60)

print(h, m)