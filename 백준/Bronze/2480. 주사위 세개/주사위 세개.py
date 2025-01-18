from collections import Counter

dices = Counter(list(map(int, input().split()))).most_common()

if len(dices) == 1:
    print(10000 + dices[0][0] * 1000)
elif len(dices) == 2:
    print(1000 + dices[0][0] * 100)
elif len(dices) == 3:
    print(max(dices, key=lambda x: x[0])[0] * 100)