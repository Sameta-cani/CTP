import sys

input = sys.stdin.readline

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

while True:
    day, month, year = map(int, input().split())
    if day == 0 and month == 0 and year == 0:
        break

    count = 0
    for m in range(1, month):
        if m in (1, 3, 5, 7, 8, 10, 12):
            count += 31
        elif m in (4, 6, 9, 11):
            count += 30
        else:
            if is_leap_year(year):
                count += 29
            else:
                count += 28
    count += day

    print(count)