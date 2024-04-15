import sys

input = sys.stdin.readline

dp = [0, 1, 1] + [0] * 20

for i in range(3, 21):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[int(input())])