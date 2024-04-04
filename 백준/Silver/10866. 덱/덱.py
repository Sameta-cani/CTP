from collections import deque
import sys

input = sys.stdin.readline

dq = deque()

for _ in range(int(input())):
    command = input().split()
    oper = command[0]

    if oper == 'push_front':
        dq.appendleft(int(command[1]))
    elif oper == 'push_back':
        dq.append(int(command[1]))
    elif oper == 'pop_front':
        print(dq.popleft() if dq else -1)
    elif oper == 'pop_back':
        print(dq.pop() if dq else -1)
    elif oper == 'size':
        print(len(dq))
    elif oper == 'empty':
        print(0 if dq else 1)
    elif oper == 'front':
        print(dq[0] if dq else -1)
    elif oper == 'back':
        print(dq[-1] if dq else -1)