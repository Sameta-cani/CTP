L, P = map(int, input().split())
total = L * P

ans = list(map(int, input().split()))

for val in ans:
    print(val - total, end=' ')