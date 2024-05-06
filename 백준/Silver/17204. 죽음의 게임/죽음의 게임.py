from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
data = [int(input()) for _ in range(N)]
visited = [False] * N

queue = deque([0])

ans = -1
cnt = 0
while queue:
    now = queue.popleft()
    if now == K:
        ans = cnt
        break
    
    if not visited[now]:
        cnt += 1
        visited[now] = True
        queue.append(data[now])

print(ans)