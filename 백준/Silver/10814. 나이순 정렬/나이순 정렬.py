data = [tuple(input().split()) for _ in range(int(input()))]

data.sort(key=lambda x: int(x[0]))

for val in data:
    print(*val)