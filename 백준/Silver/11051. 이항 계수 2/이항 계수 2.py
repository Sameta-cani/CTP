N, K = map(int, input().split())

K = (N - K) if N // 2 < K else K
mod = 10007

if K == 0:
    print(1)
else:
    dp = [0] * K
    dp[0] = N - K + 1
    for i in range(1, K):
        dp[i] = dp[i - 1] * (dp[0] + i) // (i + 1)

    print(dp[-1] % mod)