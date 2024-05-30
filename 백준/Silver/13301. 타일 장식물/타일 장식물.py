import sys

input = sys.stdin.readline

N = int(input())

dp = [1, 1] + [0] * 78

for i in range(2, 80):
    dp[i] = dp[i - 2] + dp[i - 1]
    
print(dp[N] * 2 + dp[N - 1] * 2)