import sys

input = sys.stdin.readline

N, K = map(int, input().split())
target_str = str(K)

# 특정 숫자가 포함된 시간, 분, 초의 개수를 미리 계산
def count_with_target(limit: int, target: str) -> int:
    count = 0
    for i in range(limit):
        if target in f"{i:02d}":  # 문자열 'target'이 포함된 경우를 찾음
            count += 1
    return count

# 시간, 분, 초 각각에 대해 'K'가 포함된 경우의 수 계산
count_hours_with_k = count_with_target(N + 1, target_str)   # 시간은 0시부터 N시까지
count_minutes_with_k = count_with_target(60, target_str)    # 분은 0분부터 59분까지
count_seconds_with_k = count_with_target(60, target_str)    # 초는 0초부터 59초까지

# 각각 'K'가 포함되지 않은 경우의 수 계산
total_hours = N + 1
total_minutes = 60
total_seconds = 60

count_hours_without_k = total_hours - count_hours_with_k
count_minutes_without_k = total_minutes - count_minutes_with_k
count_seconds_without_k = total_seconds - count_seconds_with_k

# 총 'K'가 포함된 경우의 수 계산
total_count = (
    count_hours_with_k * total_minutes * total_seconds +  # 시간에 'K'가 포함된 경우
    count_hours_without_k * count_minutes_with_k * total_seconds +  # 분에 'K'가 포함된 경우
    count_hours_without_k * count_minutes_without_k * count_seconds_with_k  # 초에 'K'가 포함된 경우
)

print(total_count)