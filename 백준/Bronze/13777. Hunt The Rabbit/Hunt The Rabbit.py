def binary_search(array, target, start, end):
    result = []
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            result.append(mid+1)
            return result
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
        result.append(mid+1)
    return result

array = list(range(1, 51))
N = int(input())

while N != 0:
    result = binary_search(array, N, 0, len(array)-1)
    print(*result)
    N = int(input())