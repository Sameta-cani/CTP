import sys

input = sys.stdin.readline

A, B = input().split()

num1, num2 = '5', '6'
min_value, max_value = 0, 0
for value in (A, B):
    trans_value = int(value.replace(num2, num1))
    min_value += trans_value
    trans_value = int(value.replace(num1, num2))
    max_value += trans_value

print(min_value, max_value)