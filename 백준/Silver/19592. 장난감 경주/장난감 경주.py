T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())
    Vs = list(map(int, input().split()))

    # base 보다 커야 단독 우승
    base_time = X / max(Vs)

    start = 0
    end = Y
    result = -1

    my_V = Vs[-1]
    if max(Vs[:-1]) < my_V:
        print(0)
    else:
        while start <= end:
            mid = (start + end) // 2
            my_time = 1 + (X - mid) / Vs[N - 1]
            if my_time == base_time:
                result = mid + 1
                break
            elif my_time > base_time:
                start = mid + 1
                result = mid + 1
            else:
                end = mid - 1

        print(-1 if result > Y else result)