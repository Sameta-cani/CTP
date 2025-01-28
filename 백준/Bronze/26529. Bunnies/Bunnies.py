dp = [0] * 46
dp[0] = 1
dp[1] = 1

for idx in range(2, len(dp)):
    dp[idx] = dp[idx - 1] + dp[idx - 2]
    
for _ in range(int(input())):
    n = int(input())
    print(dp[n])