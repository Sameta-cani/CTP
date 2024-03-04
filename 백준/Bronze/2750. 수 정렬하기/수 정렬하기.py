import sys
sys.setrecursionlimit(10**6)

# quick sort
N = int(input())
data = [int(input()) for _ in range(N)]

def quick_sort(data, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and data[left] <= data[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and data[right] >= data[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            data[right], data[pivot] = data[pivot], data[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            data[left], data[right] = data[right], data[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(data, start, right - 1)
    quick_sort(data, right + 1, end)

quick_sort(data, 0, len(data) - 1)

print(*data, sep='\n')