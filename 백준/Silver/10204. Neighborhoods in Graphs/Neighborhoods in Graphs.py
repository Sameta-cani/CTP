import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start: int, graph: list, N: int) -> list:
    distance = [INF] * (N + 1)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distance[start] = 0
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if distance[current_node] < current_distance:
            continue
        
        for adj, weight in graph[current_node]:
            new_distance = current_distance + weight
            
            if new_distance < distance[adj]:
                distance[adj] = new_distance
                heapq.heappush(priority_queue, (new_distance, adj))
                
    return distance

for _ in range(int(input())):
    data = input().strip().split()
    N, E = map(int, data[:2])
    graph = [[] for _ in range(N + 1)]
    edges_info = data[2:2 + 2 * E]

    for idx in range(0, len(edges_info), 2):
        u, v = int(edges_info[idx][1]), int(edges_info[idx + 1][1])
        graph[u].append((v, 1))
        graph[v].append((u, 1))
    
    
    start = int(data[-1][1])
    
    distance = dijkstra(start, graph, N)
    
    cnt = sum(1 for d in distance if 1 <= d <= 2)
            
    print(f"The number of supervillains in 2-hop neighborhood of {data[-1]} is {cnt}")
