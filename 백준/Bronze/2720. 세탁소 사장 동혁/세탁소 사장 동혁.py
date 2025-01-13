coin_types = [25, 10, 5, 1]

for _ in range(int(input())):
    C = int(input())
    for coin in coin_types:
        print(C // coin, end=' ')
        C %= coin
    print()