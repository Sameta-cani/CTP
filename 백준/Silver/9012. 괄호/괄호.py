for _ in range(int(input())):
    stack = []
    is_vps = True
    ps = input().strip()
    for p in ps:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack or stack[-1] == ')':
                is_vps = False
                break
            elif stack[-1] == '(':
                stack.pop()

    if stack:
        is_vps = False
    
    print('YES' if is_vps else 'NO')