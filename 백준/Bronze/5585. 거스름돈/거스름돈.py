import sys

input = sys.stdin.readline

count = 0
money = 1000 - int(input())

for coin in [500, 100, 50, 10, 5, 1]:
    count += money // coin
    money %= coin

print(count)