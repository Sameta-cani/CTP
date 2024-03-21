n = int(input())

array = list(map(int, input().split()))

dp = [0] * n # arr[n]까지 고려했을 때 최대 연속합

dp[0] = array[0]
for i in range(1, n):
    dp[i] = max(array[i], dp[i - 1] + array[i])

print(max(dp))