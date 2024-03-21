d = [0, 1, 1] + [0] * 90

for i in range(2, 93):
    d[i] = d[i - 1] + d[i - 2]

N = int(input())

print(d[N])