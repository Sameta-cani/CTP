from collections import deque

N = int(input())

array = deque(list(range(1, N + 1)))

while len(array) != 1:
    array.popleft()
    array.append(array.popleft())


print(array[0])