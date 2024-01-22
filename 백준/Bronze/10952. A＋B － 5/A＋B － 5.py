import sys

while True:
    A, B = map(int, sys.stdin.readline().rstrip().split())
    if not (A and B):
        break
    print(A + B)