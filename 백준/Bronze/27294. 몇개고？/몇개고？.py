T, S = map(int, input().split())

# 점심 시간이고 술을 먹지 않는 경우
mask = (12 <= T <= 16) and (S == 0)

if mask:
    print(320)
else:
    print(280)