d = [0] * 101

d[1] = 1
d[2] = 1

for i in range(3, 101):
    d[i] = d[i - 3] + d[i - 2]

T = int(input())

for _ in range(T):
    N = int(input())
    print(d[N])