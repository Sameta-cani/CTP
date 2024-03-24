N, K = map(int, input().split())
array = [int(input()) for _ in range(N)]

dp = [0] * (K + 1)
dp[0] = 1

for coin in array:
    for val in range(coin, K + 1):
        dp[val] += dp[val - coin]

print(dp[-1])