n = int(input())
INF = 100001

coins = [2, 5]
dp = [INF] * (n + 1)
dp[0] = 0

for coin in coins:
    for idx in range(coin, n + 1):
        dp[idx] = min(dp[idx], dp[idx - coin] + 1)
        
print(dp[n] if dp[n] != INF else -1)