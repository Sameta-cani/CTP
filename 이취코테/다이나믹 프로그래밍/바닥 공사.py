import sys

input = sys.stdin.readline

# Read the integer N
N = int(input())

# Init the DP table with appropriate size
if N == 1:
    print(1)
    exit()
elif N == 2:
    print(3)
    exit()
    
dp = [0] * (N + 1)

# Base cases
dp[1] = 1
dp[2] = 3

# Bottom-up dynamic programming approach
for idx in range(3, N + 1):
    dp[idx] = (dp[idx - 1] + 2 * dp[idx - 2]) % 796796
    
# Print the result
print(dp[N])