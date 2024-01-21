import sys

A, B = map(int, sys.stdin.readline().rstrip().split())
C = int(sys.stdin.readline().rstrip())

new_A = (A + (B + C) // 60) % 24
new_B = (B + C) % 60

print(new_A, new_B)