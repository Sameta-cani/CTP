import sys

input = sys.stdin.readline

def dfs(graph: list, x: int, y: int) -> None:
    stack = [(x, y)]
    N, M = len(graph), len(graph[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while stack:
        cx, cy = stack.pop()
        if graph[cx][cy] == 0:
            graph[cx][cy] = 1  # 방문 처리
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                    stack.append((nx, ny))

def count_ice_cream_zones(graph: list) -> int:
    N, M = len(graph), len(graph[0])
    result = 0

    for r in range(N):
        for c in range(M):
            if graph[r][c] == 0:  # 방문하지 않은 곳이라면
                dfs(graph, r, c)
                result += 1  # 새로운 영역 발견
    return result

# 입력 처리
N, M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

# 결과 출력
print(count_ice_cream_zones(graph))