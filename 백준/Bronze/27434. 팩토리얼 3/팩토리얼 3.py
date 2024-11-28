N = int(input())

res = 1
for idx in range(1, N + 1):
    res *= idx

print(res)