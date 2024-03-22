import sys
input = sys.stdin.readline

N = int(input().rstrip())
stack = []

for _ in range(N):
    command = input().rstrip().split()
    prompt = command[0]

    if prompt == 'push':
        stack.append(int(command[1]))
    elif prompt == 'pop':
        print(stack.pop() if stack else -1)
    elif prompt == 'size':
        print(len(stack))
    elif prompt == 'empty':
        print(1 if not stack else 0)
    elif prompt == 'top':
        print(stack[-1] if stack else -1)