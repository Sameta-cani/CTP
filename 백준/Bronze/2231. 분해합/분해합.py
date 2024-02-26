N = int(input())
gen = 0

for i in range(1, N):
    digits_sum = sum([int(x) for x in str(i)])
    if i + digits_sum == N:
        gen = i
        break

print(gen)