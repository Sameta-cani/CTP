def binary_search(target):
    start = 1
    end = 50
    while start <= end:
        mid = (start + end) // 2
        print(mid, end=' ')
        if mid == target:
            break
        elif mid > target:
            end = mid - 1
        else:
            start = mid + 1

while True:
    n = int(input())
    if n == 0:
        break
    
    binary_search(n)
    print()