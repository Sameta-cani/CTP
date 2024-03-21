d = [[0] * 16 for _ in range(16)]
d[1] = list(range(16))

for i in range(2, 16):
    for j in range(1, 16):
        if j == 1:
            d[i][j] = 1
        else:
            d[i][j] = d[i][j - 1] + d[i - 1][j]

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(d[k + 1][n])