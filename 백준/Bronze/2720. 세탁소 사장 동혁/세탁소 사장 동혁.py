import sys

input = sys.stdin.readline

coins = [25, 10, 5, 1]

for _ in range(int(input())):
    C = int(input())

    for coin in coins:
        print(C // coin, end=' ')
        C %= coin
    print()