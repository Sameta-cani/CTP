from collections import deque

N, K = map(int, input().split())

queue = deque(list(range(1, N + 1)))
count = 0

res = []
while queue:
    count += 1
    n = queue.popleft()
    if count == K:
        count = 0
        res.append(str(n))
    else:
        queue.append(n)

print('<' + ', '.join(res) + '>')