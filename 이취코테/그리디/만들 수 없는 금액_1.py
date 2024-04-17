import sys

input = sys.stdin.readline

# 입력
N = int(input())
coins = list(map(int, input().split()))

# 동전들을 이용하여 만들 수 있는 최대 금액 추정
max_possible_value = sum(coins)

# DP 테이블 초기화: 모든 금액을 False로 설정 (만들 수 없다고 가정)
dp = [False] * (max_possible_value + 1) 
dp[0] = True # 0원은 아무 동전도 사용하지 않고 만들 수 있음

# 모든 동전에 대하여 DP 테이블 업데이트
for coin in coins:
    for i in range(max_possible_value, coin - 1, -1):
        if dp[i - coin]:
            dp[i] = True

min_value = -1
# 만들 수 없는 최소 금액 찾기
for i in range(1, max_possible_value + 1):
    if not dp[i]:
        min_value = i

# 모든 금액을 만들 수 있다면, 최대 금액 + 1 반환
print(min_value if min_value != -1 else max_possible_value + 1)