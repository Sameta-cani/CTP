import sys

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    data = list(map(int, input().split()))
    for j, val in enumerate(data, start=1):
        if val == 1:
            graph[i][j] = 1
            
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
for row in range(1, N + 1):
    for col in range(1, N + 1):
        if graph[row][col] == INF:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print()