S = input()

time = 0
for c in S:
    # 문자에 대한 다이얼 시간 계산
    dial_time = (ord(c) - ord('A')) // 3 + 3
    # 'S', 'V', 'Y', 'Z'는 하나 앞의 그룹에 속함
    if c in 'SVYZ':
        dial_time -= 1
    time += dial_time

print(time)
