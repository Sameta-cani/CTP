N = int(input())  # 포도주 잔의 개수 입력
array = [int(input()) for _ in range(N)]  # 포도주 배열 입력

# DP 초기화
dp = [0] * N

dp[0] = array[0]
if N > 1:
    dp[1] = array[0] + array[1]
if N > 2:
    dp[2] = max(dp[1], array[0] + array[2], array[1] + array[2])

for i in range(3, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i], dp[i - 3] + array[i - 1] + array[i])

print(max(dp))  # 마지막 잔을 마시지 않는 경우도 고려해 최댓값 출력