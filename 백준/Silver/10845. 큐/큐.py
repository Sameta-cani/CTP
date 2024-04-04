from collections import deque
import sys

input = sys.stdin.readline

queue = deque()

for _ in range(int(input())):
    oper = input().split()

    if len(oper) == 1:
        oper = oper[0]
        if oper == 'pop':
            if not queue:
                print(-1)
            else:
                print(queue.popleft())
        elif oper == 'size':
            print(len(queue))
        elif oper == 'empty':
            print(1 if not queue else 0)
        elif oper == 'front':
            if not queue:
                print(-1)
            else:
                print(queue[0])
        elif oper == 'back':
            if not queue:
                print(-1)
            else:
                print(queue[-1])
    else:
        queue.append(int(oper[1]))