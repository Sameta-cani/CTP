import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())

graph = [[INF] * (N + 1) for _ in range(N + 1)]
first_visit = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    graph[a][a] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c
    first_visit[a][b] = b
    first_visit[b][a] = a

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if graph[a][b] > graph[a][k] + graph[k][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                first_visit[a][b] = first_visit[a][k]
                first_visit[b][a] = first_visit[b][k]

for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            print('-', end=" ")
        else:
            print(first_visit[a][b], end=" ")
    print()