import sys

input = sys.stdin.readline

day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, input().split())

base = (sum(day_of_month[1:x]) + y) % 7

if base == 0:
    print('SUN')
elif base == 1:
    print('MON')
elif base == 2:
    print('TUE')
elif base == 3:
    print('WED')
elif base == 4:
    print('THU')
elif base == 5:
    print('FRI')
elif base == 6:
    print('SAT')