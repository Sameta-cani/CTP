import sys

input = sys.stdin.readline
INF = int(1e9)

N = int(input())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    info = input().strip()
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0
        if info[j - 1] == 'Y':
            graph[i][j] = 1
            
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    
max_value = -1            
for row in range(1, N + 1):
    cnt = 0
    for col in range(1, N + 1):
        if 1 <= graph[row][col] <= 2:
            cnt += 1
    max_value = max(max_value, cnt)
    
print(max_value)