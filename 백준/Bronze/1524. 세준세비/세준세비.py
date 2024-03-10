T = int(input())

for _ in range(T):
    input()
    N, M = map(int, input().split())
    S = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)

    while S and B:
        if S[-1] >= B[-1]:
            B.pop()
        else:
            S.pop()

    if S:
        print('S')
    elif B:
        print('B')
    else:
        print('C')