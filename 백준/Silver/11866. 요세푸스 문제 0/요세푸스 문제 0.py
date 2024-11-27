from collections import deque

N, K = map(int, input().split())
queue = deque(range(1, N + 1))

del_order = []

while queue:
    queue.rotate(-(K - 1))
    del_order.append(str(queue.popleft()))

print("<" + ", ".join(del_order) + ">")