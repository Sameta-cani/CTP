def next_bus_time(s, i, c, T):
    if T <= s:
        return s - T
    if s + i * (c - 1) < T:
        return float('inf')
    cycle_count = (T - s + i - 1) // i
    next_time = s + cycle_count * i
    return next_time - T

N, T = map(int, input().split())
min_wait_time = float('inf')

for _ in range(N):
    s, i, c = map(int, input().split())
    wait_time = next_bus_time(s, i, c, T)
    min_wait_time = min(min_wait_time, wait_time)

if min_wait_time < float('inf'):
    print(min_wait_time)
else:
    print(-1)
