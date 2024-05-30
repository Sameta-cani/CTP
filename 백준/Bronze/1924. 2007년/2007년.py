import sys

input = sys.stdin.readline

day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, input().split())

base = (sum(day_of_month[1:x]) + y) % 7

weekdays = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

print(weekdays[base])