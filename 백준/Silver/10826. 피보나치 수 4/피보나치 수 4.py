N = int(input())

if N < 2:
    print(N)
else:
    x, y = 0, 1
    for _ in range(2, N + 1):
        x, y = y, x + y

    print(y)