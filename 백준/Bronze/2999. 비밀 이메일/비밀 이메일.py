import sys

input = sys.stdin.readline

msg = input().rstrip()

N = len(msg)

for i in range(1, int(N**(0.5)) + 1):
    if N % i == 0:
        R, C = i, N // i
        
for i in range(R):
    for j in range(i, N, R):
        print(msg[j], end='')