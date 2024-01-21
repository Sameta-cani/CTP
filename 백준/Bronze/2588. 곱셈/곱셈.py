import sys

exp1 = int(sys.stdin.readline().rstrip())
exp2 = int(sys.stdin.readline().rstrip())

digits_of_exp2 = str(exp2)

# exp2의 각 자릿수에 대해 exp1과의 곱을 역순으로 출력
for digit in reversed(digits_of_exp2):
    print(exp1 * int(digit))

# 두 수의 총 곱 출력
print(exp1 * exp2)