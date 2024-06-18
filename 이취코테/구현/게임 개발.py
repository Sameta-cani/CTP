import sys

input = sys.stdin.readline

# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
visited = [[0] * M for _ in range(N)]

# 현재 캐릭터의 x 좌표, y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
visited[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
map_info = [list(map(int, input().split())) for _ in range(N)]

# 북, 동, 남, 서 방향 정의
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def turn_left(current_direction: int) -> int:
    return (current_direction - 1) % 4

# 시뮬레이션 시작
cnt = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    direction = turn_left(direction)
    nx, ny = x + directions[direction][0], y + directions[direction][1]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if visited[nx][ny] == 0 and map_info[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        cnt += 1
        turn_time = 0
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx, ny = x - directions[direction][0], y - directions[direction][1]
        if map_info[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0
        
# 정답 출력
print(cnt)