import sys

input = sys.stdin.readline

# H를 입력받기
h = int(input())
target_str = '3'

# 특정 숫자가 포함된 시간, 분, 초의 개수를 미리 계산
def count_with_target(limit: int) -> int:
    count = 0
    for i in range(limit):
        count += target_str in f"{i:02d}"
    return count

# 시간, 분, 초 각각에 대해 '3'이 포함된 경우의 수 계산
count_hours_with_three = count_with_target(h + 1) # 시간은 0시부터 h시까지
count_minutes_with_three = count_with_target(60) # 분은 0분부터 59분까지
count_seconds_with_three = count_with_target(60) # 초는 0초부터 59초까지

# 각각 '3'이 포함되지 않은 경우의 수 계산
total_hours = h + 1
total_minutes = 60
total_seconds = 60

count_hours_without_three = total_hours - count_hours_with_three
count_minutes_without_three = total_minutes - count_minutes_with_three
count_seconds_without_three = total_seconds - count_seconds_with_three

# 총 '3'이 포함된 경우의 수 계산
total_count = (
    count_hours_with_three * total_minutes * total_seconds + # 시간에 '3'이 포함된 경우
    count_hours_without_three * count_minutes_with_three * total_seconds + # 분에 '3'이 포함된 경우
    count_hours_without_three * count_minutes_without_three * count_seconds_with_three # 초에 '3'이 포함된 경우
)

print(total_count)