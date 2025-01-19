N, M = map(int, input().split())
maps = [input().strip()[::-1] for _ in range(N)]

for row in maps:
    print(*row, sep='')