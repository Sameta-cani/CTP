import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][k] and graph[k][b]:
                graph[a][b] = 1

for row in graph:
    print(*row)