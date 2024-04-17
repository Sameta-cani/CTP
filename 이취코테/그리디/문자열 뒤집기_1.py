import sys

input = sys.stdin.readline

data = input()

count = 0
prev = data[0]
for digit in data[1:]:
    if prev != digit: # 이전 문자와 현재 문자가 다르다면
        count += 1 # 다를 때의 경우를 모두 더해줌
    prev = digit # 이전 문자 갱신

print(count // 2) # 답은 경우를 2로 나눈 값