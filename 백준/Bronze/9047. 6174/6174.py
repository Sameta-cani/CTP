T = int(input())

for _ in range(T):
    N = input()

    count = 0

    while True:
        if int(N) == 6174:
            print(count)
            break
        list_N = N.zfill(4)
        max_N = int(''.join(sorted(list_N, reverse=True)))
        min_N = int(''.join(sorted(list_N)))
        N = str(max_N - min_N).zfill(4)
        count += 1
