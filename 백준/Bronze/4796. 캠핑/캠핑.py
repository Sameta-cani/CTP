import sys

input = sys.stdin.readline

test_case = 0
while True:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break

    test_case += 1
    res = (V // P) * L + min((V % P), L)

    print(f"Case {test_case}: {res}")