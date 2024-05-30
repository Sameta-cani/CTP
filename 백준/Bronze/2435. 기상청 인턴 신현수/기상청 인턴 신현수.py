import sys

input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int, input().split()))

dp = [0] * (N - K + 1)

for idx in range(len(dp)):
    dp[idx] = sum(data[idx:idx+K])
    
print(max(dp))