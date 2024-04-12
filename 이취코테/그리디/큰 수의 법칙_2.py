import sys

input = sys.stdin.readline

# N, M, K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[N - 1] # 가장 큰 수
second = data[N - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(M / (K + 1)) * K
count += M % (K + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (M - count) * second # 두 번째로 큰 수 더하기

print(result)