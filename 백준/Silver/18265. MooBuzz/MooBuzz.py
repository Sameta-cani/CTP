N = int(input())

start = 1
end = int(10e9)

while start <= end:
    mid = (start + end) // 2
    
    cumsum = mid - (mid // 3) - (mid // 5) + mid // 15
    
    if cumsum == N:
        while (mid % 3 == 0) or (mid % 5 == 0):
            mid -= 1
        print(mid)
        break
    elif cumsum < N:
        start = mid + 1
    else:
        end = mid - 1
