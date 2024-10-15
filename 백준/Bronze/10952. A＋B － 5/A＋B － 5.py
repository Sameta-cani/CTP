import sys
input = sys.stdin.readline

A, B = map(int, input().split())

while A and B:
    print(A + B)
    A, B = map(int, input().split())