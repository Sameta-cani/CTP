A, K = map(int, input().split())

dp = [float('inf')] * (K + 1)
dp[A] = 0

for idx in range(A + 1, K + 1):
    dp[idx] = dp[idx - 1] + 1
    
    if idx % 2 == 0:
        dp[idx] = min(dp[idx], dp[idx // 2] + 1)
    
print(dp[K])