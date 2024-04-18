import sys

input = sys.stdin.readline

N, M = map(int, input().split())
end_time = {index: 0 for index in range(1, N + 1)}

for _ in range(M):
    k, s, e = map(int, input().split())
    final = end_time.get(k)
    if s >= final:
        end_time[k] = e
        print('YES')
    else:
        print('NO')