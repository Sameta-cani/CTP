import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N = int(input().rstrip())
    Note1 = set(map(int, input().rstrip().split()))
    M = int(input().rstrip())
    Note2 = list(map(int, input().rstrip().split()))

    for val in Note2:
        if val in Note1:
            print(1)
        else:
            print(0)