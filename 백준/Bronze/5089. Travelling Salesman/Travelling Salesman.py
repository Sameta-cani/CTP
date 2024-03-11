weeks = 1
N = int(input())

while N != 0:
    n_towns = len({input() for _ in range(N)})
    print(f'Week {weeks} {n_towns}')

    weeks += 1
    N = int(input())