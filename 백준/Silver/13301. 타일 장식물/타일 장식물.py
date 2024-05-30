import sys

input = sys.stdin.readline

N = int(input())

dp = [4, 6] + [0] * 80

for i in range(2, N + 1):
    dp[i] = dp[i - 2] + dp[i - 1]
    
print(dp[N - 1])