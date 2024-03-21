N = int(input())

d = [0, 1, 1] + [0] * 45

for i in range(3, 46 + 1):
    d[i] = d[i - 1] + d[i - 2]

for _ in range(N):
    x = int(input())
    print(d[x + 1])