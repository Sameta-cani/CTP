import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())
I, J, K = map(int, input().split())

base = min(A / I, B / J, C / K)

I *= base
J *= base
K *= base

print(A - I, B - J, C - K)