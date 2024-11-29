K, N = map(int, input().split())
data = [int(input()) for _ in range(K)]

start = 1
end = max(data)
result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum(val // mid for val in data)
    
    if cnt < N:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)