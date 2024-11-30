n = int(input())
data = [int(input()) for _ in range(n)]

stack = []
result = []
cur = 1

for val in data:
    while cur <= val:
        stack.append(cur)
        result.append('+')
        cur += 1
    
    if stack[-1] == val:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        break
else:
    print('\n'.join(result))