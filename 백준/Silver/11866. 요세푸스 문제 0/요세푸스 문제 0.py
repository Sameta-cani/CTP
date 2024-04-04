from collections import deque

N, K = map(int, input().split())

queue = deque(range(1, N + 1))

elimination_order = []

while queue:
    queue.rotate(-(K - 1))
    elimination_order.append(str(queue.popleft()))

print("<" + ", ".join(elimination_order) + ">")