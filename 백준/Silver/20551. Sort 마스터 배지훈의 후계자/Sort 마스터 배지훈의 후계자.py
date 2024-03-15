import sys
input = sys.stdin.readline

def binary_search_first(array, target):
    start, end = 0, len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if (mid == 0 or array[mid - 1] < target) and array[mid] == target:
            return mid
        elif array[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    
N, M = map(int, input().rstrip().split())
array = sorted([int(input().rstrip()) for _ in range(N)])

for _ in range(M):
    D = int(input().rstrip())
    index = binary_search_first(array, D)
    print(index if index != None else -1)