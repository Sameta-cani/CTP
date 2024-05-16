from collections import deque
import sys

input = sys.stdin.readline

front = deque(list(input().strip()))
back = deque([])

for _ in range(int(input())):
    command = input().rstrip().split()
    if command[0] == 'L':
        if front:
            back.appendleft(front.pop())
    elif command[0] == 'D':
        if back:
            front.append(back.popleft())
    elif command[0] == 'B':
        if front:
            front.pop()
    elif command[0] == 'P':
        front.append(command[1])
        
print(*(front + back), sep='')