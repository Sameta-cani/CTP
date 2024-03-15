import sys
input = sys.stdin.readline

def first(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return start

def last(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return end

def count_by_range(array, data):
    n = len(array)
    kind = data[0]
    if kind == 1:
        a = first(array, data[1], 0, n - 1)
        b = last(array, array[-1], 0, n - 1)  # 마지막 요소를 직접 사용
    elif kind == 2:
        a = last(array, data[1], 0, n - 1) + 1
        b = last(array, array[-1], 0, n - 1)  # 마지막 요소를 직접 사용
    else:
        a = first(array, data[1], 0, n - 1)
        b = last(array, data[2], 0, n - 1)
    
    return b - a + 1

N, M = map(int, input().rstrip().split())
array = sorted(list(map(int, input().rstrip().split())))

for _ in range(M):
    data = list(map(int, input().rstrip().split()))
    result = count_by_range(array, data)
    print(result)
