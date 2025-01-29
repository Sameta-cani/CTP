N = int(input())

dp = [0] * (N + 1)
for idx in range(2, N + 1):
    dp[idx] = (idx - 1) + dp[idx - 1]
    
print(dp[N])