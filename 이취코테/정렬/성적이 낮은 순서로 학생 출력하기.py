import sys

input = sys.stdin.readline

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for idx in range(K):
    # A의 원소가 B의 원소보다 작은 경우
    if a[idx] < b[idx]:
        # 두 원소를 교체
        a[idx], b[idx] = b[idx], a[idx]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break
    
print(sum(a))