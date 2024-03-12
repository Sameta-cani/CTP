import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))

start = 0
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for val in array:
        if val > mid:
            total += (val - mid)

    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)