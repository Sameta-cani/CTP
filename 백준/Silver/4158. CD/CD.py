import sys

input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

while True:
    N, M = map(int, input().split())
    
    if N == 0 and M == 0:
        break
    
    N_array = list(int(input()) for _ in range(N))
    M_array = list(int(input()) for _ in range(M))
    
    ptr1, ptr2 = 0, 0
    cnt = 0
    while ptr1 < N and ptr2 < M:
        if N_array[ptr1] < M_array[ptr2]:
            ptr1 += 1
        elif N_array[ptr1] > M_array[ptr2]:
            ptr2 += 1
        else:
            cnt += 1
            ptr1 += 1
            ptr2 += 1
            
    print(cnt)