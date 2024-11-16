for _ in range(int(input())):
    score = 0
    stack = list()
    for ch in input().strip():
        if ch == 'O':
            stack.append(len(stack) + 1)
        elif ch == 'X':
            score += sum(stack)
            stack.clear()
    score += sum(stack)
    print(score)