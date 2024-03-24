# 거스름돈 액수 N 입력
N = int(input())

# 거스름돈 종류
array = [2, 5]

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [100001] * (N + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
dp[0] = 0
for val in array:
    for i in range(val, N + 1):
        dp[i] = min(dp[i], dp[i - val] + 1)

print(dp[N] if dp[N] != 100001 else -1)