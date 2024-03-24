import math

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    N_fac = math.factorial(N)

    dp = [0] * N
    dp[0] = (M - N + 1)

    for i in range(1, N):
        dp[i] = dp[i - 1] * (dp[0] + i)

    print(dp[-1] // N_fac)