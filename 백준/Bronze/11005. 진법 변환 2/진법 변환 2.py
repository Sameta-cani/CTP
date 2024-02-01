import sys

N, B = map(int, sys.stdin.readline().rstrip().split())

converted_number = ''

while N >= B:
    remainder = N % B
    if remainder >= 10:
        converted_number = chr(remainder + 55) + converted_number
    else:
        converted_number = str(remainder) + converted_number
    N //= B

# 마지막 남은 수 처리
if N >= 10:
    converted_number = chr(N + 55) + converted_number
else:
    converted_number = str(N) + converted_number

print(converted_number)