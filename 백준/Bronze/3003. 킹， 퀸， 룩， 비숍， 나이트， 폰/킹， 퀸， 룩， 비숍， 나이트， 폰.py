data = list(map(int, input().split()))

for a, b in zip((1, 1, 2, 2, 2, 8), data):
    print(a - b, end=' ')