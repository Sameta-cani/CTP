N = int(input())

start, end = 1, N

while start <= end:
    mid = (start + end) // 2
    if mid**2 == N:
        break
    elif mid**2 > N:
        end = mid - 1
    else:
        start = mid + 1

print(mid)