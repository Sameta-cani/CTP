import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start: int, graph: list) -> list:
    distance = [INF] * (N + 1)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distance[start] = 0
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if distance[current_node] < current_distance:
            continue
        
        for adj, weight in graph[current_node]:
            distance_via_current = current_distance + weight
            
            if distance_via_current < distance[adj]:
                distance[adj] = distance_via_current
                heapq.heappush(priority_queue, (distance_via_current, adj))
                
    return distance

for _ in range(int(input())):
    data = input().strip().split()
    N, E = map(int, data[:2])
    graph = [[] for _ in range(N + 1)]
    edges_info = data[2:2+2*E]

    for idx in range(0, len(edges_info), 2):
        edge = edges_info[idx:idx+2]
        u, v = int(edge[0][1]), int(edge[1][1])
        graph[u].append((v, 1))
        graph[v].append((u, 1))
    
    
    start = int(data[-1][1])
    distance = dijkstra(start, graph)
    
    cnt = 0
    for dist in distance:
        if 1 <= dist <= 2:
            cnt += 1
            
    print(f"The number of supervillains in 2-hop neighborhood of {data[-1]} is {cnt}")
    