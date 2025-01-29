K = int(input())

dp = [0] * (K + 2)
dp[1] = 1

for idx in range(2, K + 2):
    dp[idx] = dp[idx - 1] + dp[idx - 2]
    
print(dp[K + 1] - dp[K], dp[K])