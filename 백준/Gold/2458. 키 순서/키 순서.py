import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    graph[a][a] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

count = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        is_possible = True
        if graph[a][b] == INF and graph[b][a] == INF:
            is_possible = False
            break
    count += is_possible

print(count)