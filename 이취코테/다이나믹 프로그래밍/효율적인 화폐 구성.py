import sys

input = sys.stdin.readline

# Read integers N (number of coin types) and M (desired amount)
N, M = map(int, input().split())
# Read the coin denominations
coins = [int(input()) for _ in range(N)]

# Init the DP table with a large value (infinity substitute)
dp = [10001] * (M + 1)
dp[0] = 0 # Base case: 0 amount requires 0 coins

# Dynamic programming approach (bottom-up)
for coin in coins:
    for j in range(coin, M + 1):
        if dp[j - coin] != 10001:
            dp[j] = min(dp[j], dp[j - coin] + 1)
            
# Print the result
result = dp[M] if dp[M] != 10001 else -1
print(result)