import sys

input = sys.stdin.readline

# 정수 N을 입력받기
N = int(input())
# 모든 식량 정보 입력받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
dp[0] = array[0]
dp[1] = max(array[0], array[1])
for idx in range(2, N):
    dp[idx] = max(dp[idx - 1], dp[idx - 2] + array[idx])
    
# 계산된 결과 출력
print(dp[N - 1])