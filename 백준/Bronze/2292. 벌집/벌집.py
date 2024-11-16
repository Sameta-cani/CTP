N = int(input())

cur = 1
for i in range(N):
    if cur + i * 6 >= N:
        print(i + 1)
        break
    cur += i * 6