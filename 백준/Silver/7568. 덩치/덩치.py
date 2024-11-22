data = [tuple(map(int, input().split())) for _ in range(int(input()))]

for i in data:
    rank = 1
    for j in data:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')