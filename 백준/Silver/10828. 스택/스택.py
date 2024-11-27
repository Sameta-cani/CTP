import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    command = input().rstrip().split()
    prompt = command[0]

    if prompt == 'push':
        stack.append(int(command[1]))
    elif prompt == 'pop':
        print(stack.pop() if stack else -1)
    elif prompt == 'size':
        print(len(stack))
    elif prompt == 'empty':
        print(0 if stack else 1)
    elif prompt == 'top':
        print(stack[-1] if stack else -1)