import sys

input = sys.stdin.readline

sent = input()
stack = []

trans = {None: 'K', 
        'A': 'K', 
        'K': 'O', 
        'O': 'R', 
        'R': 'E',
        'E': 'A' }

for data in sent:
    if data == (trans.get(stack[-1] if stack else None)):
        stack.append(data)

print(len(stack))