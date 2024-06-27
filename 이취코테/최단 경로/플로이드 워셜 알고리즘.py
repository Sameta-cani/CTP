import sys

input = sys.stdin.readline
INF = int(1e9) # Infinity represented by a large number

# Number of nodes and edges
N = int(input())
M = int(input())

# Init the graph with infinity
graph = [[INF] * (N + 1) for _ in range(N + 1)]

# Distance to self is zero
for i in range(1, N + 1):
    graph[i][i] = 0
    
# Input edges
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c) # In case of multiple edges, take the smallest one
    
# Floyd-Warshall algorithm
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
            
# Ouput the result
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            print("INFINITY", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()