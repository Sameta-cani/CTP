N = int(input())

if N == 1:
    print(int(input()))
elif N == 2:
    print(sum(int(input()) for _ in range(2)))
else:
    points = [0] + [int(input()) for _ in range(N)]
    dp = [0] * (N + 1)

    dp[1] = points[1]
    dp[2] = points[1] + points[2]

    for idx in range(3, N + 1):
        dp[idx] = max(dp[idx - 3] + points[idx - 1], dp[idx - 2]) + points[idx]

    print(dp[N])