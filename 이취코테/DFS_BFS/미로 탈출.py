from collections import deque
import sys

input = sys.stdin.readline

# N, M을 공백으로 구분하여 입력받기
N, M = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = [list(map(int, input().strip())) for _ in range(N)]

# 이동할 네 방향 정의 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# BFS 소스코드 구현
def BFS(x: int, y: int) -> int:
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 범위를 벗어나지 않고, 벽이 아닌 경우
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                # 방문한 칸을 최단 거리로 업데이트
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[N - 1][M - 1]

print(BFS(0, 0))