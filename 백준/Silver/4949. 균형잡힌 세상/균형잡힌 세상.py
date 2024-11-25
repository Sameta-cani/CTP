from collections import deque
import sys
input = sys.stdin.readline

while True:
    sen = input().rstrip()
    if sen == '.':
        break
    stack = deque()
    is_balanced = True
    for ch in sen:
        if ch in '([':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_balanced = False
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                is_balanced = False
                break
        
    if stack:
        is_balanced = False
    print('yes' if is_balanced else 'no')