A, B = map(int, input().split())
K, X = map(int, input().split())

lower = max(A, K - X)
upper = min(B, K + X)

res = upper - lower + 1

print(res if res > 0 else 'IMPOSSIBLE')