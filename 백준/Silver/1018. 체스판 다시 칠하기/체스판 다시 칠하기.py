N, M = map(int, input().split())
maps = [input() for _ in range(N)]
counts = []

for x in range(N - 7):
    for y in range(M - 7):
        for first_color in ['B', 'W']:
            count = 0
            for i in range(8):
                for j in range(8):
                    expected_color = first_color if (i + j) % 2 == 0 else 'B' if first_color == 'W' else 'W'
                    if maps[x+i][y+j] != expected_color:
                        count += 1
            counts.append(count)

print(min(counts))