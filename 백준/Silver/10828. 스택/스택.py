import sys
input = sys.stdin.readline

class stack():
    def __init__(self):
        self.array = list()
    def size(self):
        return len(self.array)
    def push(self, value):
        self.array.append(value)
    def pop(self):
        if self.size() <= 0:
            return -1
        else:
            value = self.array.pop()
            return value
    def empty(self):
        return 1 if self.size() == 0 else 0
    def top(self):
        return self.array[-1] if self.size() > 0 else -1
    
Stack = stack()

N = int(input().rstrip())

for _ in range(N):
    command = input().rstrip().split(' ')
    prompt = command[0]
    if prompt == 'push':
        Stack.push(int(command[1]))
    elif prompt == 'pop':
        print(Stack.pop())
    elif prompt == 'size':
        print(Stack.size())
    elif prompt == 'empty':
        print(Stack.empty())
    elif prompt == 'top':
        print(Stack.top())