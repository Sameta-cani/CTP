import sys

input = sys.stdin.readline

# N(가게의 부품 개수)을 입력받기
N = int(input())
array = [0] * 100001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for idx in input().split():
    array[int(idx)] = True
    
# M(손님이 확인 요청한 부품 개수)을 입력받기
M = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for val in x:
    # 해당 부품이 존재하는지 확인
    if array[val]:
        print('yes', end=' ')
    else:
        print('no', end=' ')