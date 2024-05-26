from collections import deque

def solution(dartResult: str) -> int:
    stack = deque([])
    is_prev_digit = False
    for d in dartResult:
        if d.isdigit():
            if is_prev_digit:
                stack.append(stack.pop() * 10)
                is_prev_digit = False
            else:
                stack.append(int(d))
            is_prev_digit = True
        elif d == '*':
            if len(stack) == 1:
                stack.append(stack.pop()*2)
            else:
                cur = stack.pop()
                prev = stack.pop()
                stack.append(prev*2)
                stack.append(cur*2)
        elif d == '#':
            stack.append(stack.pop()*(-1))
        elif d.isalpha():
            is_prev_digit = False
            if d == 'S':
                continue
            elif d == 'D':
                stack.append(stack.pop()**2)
            elif d == 'T':
                stack.append(stack.pop()**3)
    return sum(stack)