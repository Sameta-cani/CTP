import sys

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    data = input()
    for b in range(1, N + 1):
        if a == b:
            graph[a][b] = 0
        else:
            if data[b-1] == 'Y':
                graph[a][b] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

max_count = -INF
for a in range(1, N + 1):
    count = 0
    for b in range(1, N + 1):
        if a != b and 0 < graph[a][b] <= 2:
            count += 1
    max_count = max(max_count, count)

print(max_count)