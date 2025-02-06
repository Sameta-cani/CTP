from collections import deque
import sys

input = sys.stdin.readline

queue = deque([])
for _ in range(int(input())):
    command = input().strip().split()
    prompt = command[0]
    
    if prompt == 'push':
        queue.append(command[1])
    elif prompt == 'pop':
        print(queue.popleft() if queue else -1)
    elif prompt == 'size':
        print(len(queue))
    elif prompt == 'empty':
        print(0 if queue else 1)
    elif prompt == 'front':
        print(queue[0] if queue else -1)
    elif prompt == 'back':
        print(queue[-1] if queue else -1)
