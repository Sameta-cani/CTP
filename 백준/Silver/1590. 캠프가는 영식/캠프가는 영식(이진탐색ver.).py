def binary_search(array, T):
    start, end = 0, len(array) - 1
    result = None  # 초기값 설정
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= T:
            result = array[mid]
            end = mid - 1
        else:
            start = mid + 1
    return result


N, T = map(int, input().split())
array = list()
min_bus = list()

for _ in range(N):
    s, i, c = map(int, input().split())
    if s == T:
        min_bus.append(0)
        break
    last_bus_time = s + i * (c-1)
    if last_bus_time < T:
        continue
    else:
        result = binary_search(list(range(s, s + i * c, i)), T)
        if result is not None:
            min_bus.append(result - T)


if min_bus:
    print(min(min_bus))
else:
    print(-1)
