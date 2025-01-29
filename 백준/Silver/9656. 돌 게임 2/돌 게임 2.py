N = int(input())

dp = [0] * (N + 1)
dp[1] = 1
if N > 1:
    dp[2] = 2
    
for idx in range(3, N + 1):
    dp[idx] = min(dp[idx - 1] + 1, dp[idx - 3] + 1)
    
print("CY" if dp[N] % 2 == 1 else "SK")