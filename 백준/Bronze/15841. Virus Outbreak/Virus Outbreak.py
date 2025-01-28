import sys

input = sys.stdin.readline

dp = [0] * 491
dp[1] = 1

for idx in range(2, len(dp)):
    dp[idx] = dp[idx - 1] + dp[idx - 2]
    
while True:
    n = int(input())
    
    if n == -1:
        break
    
    print(f"Hour {n}: {dp[n]} cow(s) affected")