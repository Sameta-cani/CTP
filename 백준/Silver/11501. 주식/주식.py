T = int(input())

for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))
    profit = 0
    max_value = stocks[-1]

    for price in reversed(stocks[:-1]):
        if max_value < price:
            max_value = price
        else:
            profit += (max_value - price)

    print(profit)