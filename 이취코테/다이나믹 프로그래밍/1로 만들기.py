import sys

input = sys.stdin.readline

# Read the integer input
x = int(input())

# Init the DP table with appropriate size
dp = [0] * (x + 1)

# Dynamic programming to find the minimum steps to reduce x to 1
for idx in range(2, x + 1):
    # Start with the operation of subtracting 1
    dp[idx] = dp[idx - 1] + 1
    # Check division by 2
    if idx % 2 == 0:
        dp[idx] = min(dp[idx], dp[idx // 2] + 1)
    # Check division by 3
    if idx % 3 == 0:
        dp[idx] = min(dp[idx], dp[idx // 3] + 1)
    # Check division by 5
    if idx % 5 == 0:
        dp[idx] = min(dp[idx], dp[idx // 5] + 1)
        
# Print the result
print(dp[x])