import sys

N = int(sys.stdin.readline().rstrip())

# 입력된 숫자를 정렬
arr = sorted([int(sys.stdin.readline().rstrip()) for _ in range(N)])

result = 0

# 각 숫자의 순위는 정렬된 배열에서의 인덱스+1입니다.
# 따라서, 각 숫자의 순위와의 차이의 절대값을 계산합니다.
for idx, value in enumerate(arr, 1):
    result += abs(value - idx)

print(result)