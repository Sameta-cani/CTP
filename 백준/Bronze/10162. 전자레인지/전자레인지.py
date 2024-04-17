import sys

input = sys.stdin.readline

times = [300, 60, 10]

T = int(input())

if T % times[-1] != 0:
    print(-1)
else:
    res = []
    for time in times:
        res.append(T // time)
        T %= time

    print(*res)