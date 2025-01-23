import sys

input = sys.stdin.readline

def binary_saerch(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(input())
N_array = list(map(int, input().split()))
N_array.sort()
M = int(input())
M_array = list(map(int, input().split()))

for item in M_array:
    result = binary_saerch(N_array, item, 0, N - 1)
    if result != None:
        print(1, end=' ')
    else:
        print(0, end=' ')