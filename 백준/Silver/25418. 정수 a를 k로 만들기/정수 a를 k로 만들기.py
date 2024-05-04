from collections import deque
import sys

input = sys.stdin.readline

A, K = map(int, input().split())

queue = deque([(A, 0)])
visited = set([A])
ans = 0

while queue:
    cur, cnt = queue.popleft()

    if cur == K:
        ans = cnt
        break

    next_steps = [cur * 2, cur + 1]
    for next_val in next_steps:
        if next_val not in visited and next_val <= 2 * K:
            visited.add(next_val)
            queue.append((next_val, cnt + 1))

print(ans)