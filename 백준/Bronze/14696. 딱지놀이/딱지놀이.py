import sys

input = sys.stdin.readline

for _ in range(int(input())):
    A = sorted(tuple(map(int, input().split()))[1:], reverse=True)
    B = sorted(tuple(map(int, input().split()))[1:], reverse=True)
    
    if A == B:
        print('D')
    else:
        tmp = sorted([A, B], reverse=True)
        if tmp[0] == A:
            print('A')
        else:
            print('B')