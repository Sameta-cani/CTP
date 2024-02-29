import sys
sys.setrecursionlimit(10**6)

N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
homes_count = []

def dfs(x, y):
    if x < 0 or x >= N or y < 0 or y >= N or graph[x][y] == 0:
        return 0
    if graph[x][y] == 1:
        graph[x][y] = -1
        # 현재 집을 카운트하고 인접한 집 탐색
        count = 1
        count += dfs(x-1, y)
        count += dfs(x+1, y)
        count += dfs(x, y-1)
        count += dfs(x, y+1)
        return count
    return 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            homes_count.append(dfs(i, j))

print(len(homes_count))  # 총 단지 수 출력
homes_count.sort()
for count in homes_count:
    print(count)
