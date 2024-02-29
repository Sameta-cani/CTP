import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    if graph[y][x] == 1:
        graph[y][x] = -1
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())

    graph = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if graph[j][i] == 1:
                dfs(i, j)
                count += 1

    print(count)