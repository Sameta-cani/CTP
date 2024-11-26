N = int(input())

dp = [1, 1] + [0] * 11

for idx in range(2, len(dp)):
    dp[idx] = idx * dp[idx - 1]

print(dp[N])