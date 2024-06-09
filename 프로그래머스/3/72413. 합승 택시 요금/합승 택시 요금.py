import sys

input = sys.stdin.readline
INF = int(1e9)

def solution(n: int, s: int, a: int, b: int, fares: list) -> int:
    answer = INF
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                graph[i][j] = 0
                break
            
    for value in fares:
        i, j, cost = value
        graph[i][j] = cost
        graph[j][i] = cost
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    for idx in range(1, n + 1):
        answer = min(answer, graph[s][idx] + graph[idx][a] + graph[idx][b])
        
    return answer