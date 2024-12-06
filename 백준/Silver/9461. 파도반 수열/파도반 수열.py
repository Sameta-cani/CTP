MAX_N = 101

dp = [0] * (MAX_N)
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for idx in range(6, MAX_N):
    dp[idx] = dp[idx - 1] + dp[idx - 5]

for _ in range(int(input())):
    N = int(input())
    print(dp[N])