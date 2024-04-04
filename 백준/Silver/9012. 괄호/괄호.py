for tc in range(int(input())):
    data = input()
    stack = []
    is_VPS = True

    for s in data:
        if s == '(':
            stack.append(s)
        else:
            if not stack:
                is_VPS = False
                break
            stack.pop()

    print('YES' if is_VPS and not stack else 'NO')