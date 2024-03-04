import sys

N = int(input())
count = [0] * 10001

for _ in range(N):
    count[int(sys.stdin.readline().rstrip())] += 1

for i in range(10001):
    for j in range(count[i]):
        print(i)