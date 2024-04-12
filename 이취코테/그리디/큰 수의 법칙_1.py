import sys

input = sys.stdin.readline

# N, M, K를 공백으로 구분하여 입력받기
N, M, K = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[-1] # 가장 큰 수
second = data[-2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(K): # 가장 큰 수를 K번 더하기
        if M == 0: # M이 0이라면 반복문 탈출
            break
        result += first
        M -= 1 # 더할 때마다 1씩 빼기
    if M == 0: # M이 0이라면 반복문 탈출
        break
    result += second # 두 번째로 큰 수를 한 번 더하기
    M -= 1 # 더할 때마다 1씩 빼기

print(result)