N = int(input())  # 돌의 개수

# DP 배열 초기화
dp = [0] * (N + 1)
dp[1] = 1
if N > 1:
    dp[2] = 2

# DP 점화식 계산
for i in range(3, N + 1):
    dp[i] = min(dp[i - 1] + 1, dp[i - 3] + 1)

# 게임 과정 횟수의 홀짝에 따라 승패 결정
if dp[N] % 2 == 1:
    print("SK")
else:
    print("CY")
