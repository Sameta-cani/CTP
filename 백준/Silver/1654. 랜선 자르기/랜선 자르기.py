import sys
input = sys.stdin.readline

K, N = map(int, input().split())
array = [int(input().rstrip()) for _ in range(K)]

start = 1
end = max(array)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for val in array:
        total += val // mid
    if total < N:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)