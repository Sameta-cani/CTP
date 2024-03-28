import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    distance = [INF] * (N + 1)
    distance[start] = 0
    q = [(0, start)]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

distance_1 = dijkstra(1)
distance_v1 = dijkstra(v1)
distance_v2 = dijkstra(v2)

path_1 = distance_1[v1] + distance_v1[v2] + distance_v2[N]
path_2 = distance_1[v2] + distance_v2[v1] + distance_v1[N]

result = min(path_1, path_2)

if result < INF:
    print(result)
else:
    print(-1)