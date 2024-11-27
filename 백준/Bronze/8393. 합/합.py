n = int(input())

dp = [0] * 10001

for idx in range(1, len(dp)):
    dp[idx] = idx + dp[idx - 1]

print(dp[n])