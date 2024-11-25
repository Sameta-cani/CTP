from collections import deque
import sys
input = sys.stdin.readline

while True:
    sen = input().rstrip()
    if sen == '.':
        break
    stack = deque(list())
    for ch in sen:
        if ch in ['(', '[']:
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(ch)
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(ch)
        
    print('no' if stack else 'yes')