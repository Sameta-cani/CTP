import sys
input = sys.stdin.readline

# 보드 크기
N = 5

# 방향 벡터: 상, 하, 좌, 우
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# DFS 함수 정의
def dfs(x, y, steps, apples):
    global found
    if apples >= 2:
        found = True
        return
    if steps == 3:
        return

    original = graph[x][y]
    graph[x][y] = -1  # 현재 위치를 장애물로 변경

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] != -1:
            dfs(nx, ny, steps + 1, apples + (1 if graph[nx][ny] == 1 else 0))

    graph[x][y] = original  # 상태 복구

# 입력 처리
graph = [list(map(int, input().split())) for _ in range(N)]
R, C = map(int, input().split())

# 결과 초기화
found = False

# DFS 탐색 시작
dfs(R, C, 0, 0)

# 결과 출력
print(1 if found else 0)
