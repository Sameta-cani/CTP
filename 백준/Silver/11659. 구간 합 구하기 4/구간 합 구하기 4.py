import sys
input = sys.stdin.readline

N, M = map(int, input().split())
data = list(map(int, input().split()))

dp = [0] * N
dp[0] = data[0]
for idx in range(1, N):
    dp[idx] = dp[idx - 1] + data[idx]

for _ in range(M):
    i, j = map(int, input().split())
    print(dp[j - 1] - (dp[i - 2] if i > 1 else 0))