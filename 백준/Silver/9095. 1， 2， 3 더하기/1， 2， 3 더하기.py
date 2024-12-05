import sys
input = sys.stdin.readline

MAX_N = 10
dp = [0] * (MAX_N + 1)
dp[1], dp[2], dp[3] = 1, 2, 4

for idx in range(4, MAX_N + 1):
    dp[idx] = dp[idx - 1] + dp[idx - 2] + dp[idx - 3]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])