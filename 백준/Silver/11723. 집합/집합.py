import sys

input = sys.stdin.readline

S = set()

for _ in range(int(input())):
    command = input().split()
    prompt = command[0]

    if prompt == 'add':
        value = int(command[1])
        S.add(value)
    elif prompt == 'remove':
        value = int(command[1])
        if value in S:
            S.remove(value)
    elif prompt == 'check':
        print(1 if int(command[1]) in S else 0)
    elif prompt == 'toggle':
        value = int(command[1])
        if value in S:
            S.remove(value)
        else:
            S.add(value)
    elif prompt == 'all':
        S = set(range(1, 21))
    elif prompt == 'empty':
        S = set()