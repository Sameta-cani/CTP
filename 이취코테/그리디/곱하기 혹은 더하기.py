import sys

input = sys.stdin.readline

data = input().rstrip()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for n in data[1:]:
    # 두 수 중에서 하나라도 1 이하인 경우, 곱하기보다는 더하기 수행
    num = int(n)
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)