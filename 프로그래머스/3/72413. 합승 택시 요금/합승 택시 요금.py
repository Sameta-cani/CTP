import sys

input = sys.stdin.readline

def solution(n: int, s: int, a: int, b: int, fares: list) -> int:
    INF = int(1e9)
    
    graph = [[INF if i != j else 0 for j in range(n + 1)] for i in range(n + 1)]
    
    for i, j, cost in fares:
        graph[i][j] = cost
        graph[j][i] = cost
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                
    answer = INF
    for idx in range(1, n + 1):
        if graph[s][idx] < INF and graph[idx][a] < INF and graph[idx][b] < INF:
            total_cost = graph[s][idx] + graph[idx][a] + graph[idx][b]
            answer = min(answer, total_cost)
            
    return answer