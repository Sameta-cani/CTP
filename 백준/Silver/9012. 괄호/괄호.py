for tc in range(int(input())):
    data = input()
    stack = []
    is_VPS = True

    for s in data:
        if s == '(':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                is_VPS = False
                break

    print('YES' if is_VPS and not stack else 'NO')