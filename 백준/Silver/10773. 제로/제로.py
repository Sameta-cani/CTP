stack = []
for _ in range(int(input())):
    val = int(input())
    if val != 0:
        stack.append(val)
    else:
        stack.pop()

print(sum(stack))