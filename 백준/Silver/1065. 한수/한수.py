def is_han(val):
    digits = [int(d) for d in str(val)]
    # 공차 구하기
    d = digits[1] - digits[0]
    # 모든 자릿수에 대해 공차가 일정한지 확인
    for i in range(2, len(digits)):
        if digits[i] - digits[i-1] != d:
            return 0
    return 1

N = int(input())
count = 99 if N > 99 else N # 99 이하의 숫자는 모두 한수

if N >= 100:
    for i in range(100, N+1):
        count += is_han(i)

print(count)