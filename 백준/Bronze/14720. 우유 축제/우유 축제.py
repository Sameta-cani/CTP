import sys

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

trans = {None: 0, 2: 0, 0: 1, 1: 2}

stack = []
for data in array:
    if data == trans.get(stack[-1] if stack else None):
        stack.append(data)

print(len(stack))