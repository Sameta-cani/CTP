from collections import Counter

def calculate_max_price(n):
    max_price = 0

    for _ in range(n):
        rolls = list(map(int, input().split()))
        data = Counter(rolls)

        if len(data) == 3:
            price = max(rolls) * 100
        elif len(data) == 2:
            common_number = data.most_common(1)[0][0]
            price = 1000 + common_number * 100
        else:
            price = 10000 + rolls[0] * 1000

        max_price = max(max_price, price)

    return max_price

n = int(input())
print(calculate_max_price(n))