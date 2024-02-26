N = int(input())

for i in range(N//5, -1, -1):
    if (N - (5 * i)) % 3 == 0:
        j = (N - (5 * i)) // 3
        min_count = i + j
        break
    else:
        min_count = -1

print(min_count)