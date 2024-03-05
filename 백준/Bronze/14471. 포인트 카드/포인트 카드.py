N, M = map(int, input().split())
count = 0
money = 0

cards = sorted([tuple(map(int, input().split())) for _ in range(M)], key=lambda x: x[0], reverse=True)

for i, _ in cards:
    if i < N:
        money += (N - i)
    count += 1
    if count >= (M - 1):
        break

print(money)