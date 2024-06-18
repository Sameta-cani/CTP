import sys

input = sys.stdin.readline

# N을 입력받기
N = int(input())
x, y = 1, 1
plans = input().rstrip().split()

# 이동 계획에 따른 좌표 변화를 딕셔너리로 정의
move_dict = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

# 이동 계획을 하나씩 확인
for plan in plans:
    if plan in move_dict: # 유효한 이동 계획인지 확인
        dx, dy = move_dict[plan]
        nx, ny = x + dx, y + dy
        
        # 공간을 벗어나는 경우 무시
        if 1 <= nx <= N and 1 <= ny <= N:
            x, y = nx, ny
            
print(x, y)