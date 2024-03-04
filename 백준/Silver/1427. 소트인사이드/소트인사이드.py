N = list(map(int, list(input())))
count = [0] * 10

for i in range(len(N)):
    count[N[i]] += 1

for i in range(len(count)-1, -1, -1):
    for j in range(count[i]):
        print(i, end='')