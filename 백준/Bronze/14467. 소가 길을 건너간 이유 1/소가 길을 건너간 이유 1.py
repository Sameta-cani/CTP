import sys

input = sys.stdin.readline

cows = [-1] * 11

cnt = 0
for _ in range(int(input())):
    number, state = map(int, input().split())
    if cows[number] == -1:
        cows[number] = state
    else:
        if cows[number] != state:
            cnt += 1
            cows[number] = state
        
print(cnt)