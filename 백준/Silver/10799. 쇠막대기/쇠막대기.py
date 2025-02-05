data = input()
stack = []
answer = 0

for idx in range(len(data)):
    if data[idx] == '(':
        stack.append(data[idx])
    else:
        if data[idx - 1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)