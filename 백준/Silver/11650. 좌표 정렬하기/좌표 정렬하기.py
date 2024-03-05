N = int(input())

array = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))

for x, y in array:
    print(f'{x} {y}')