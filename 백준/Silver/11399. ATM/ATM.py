import sys
input = sys.stdin.readline

N = int(input())
time_per = list(map(int, input().split()))

time_per.sort()
for idx in range(1, N):
    time_per[idx] = time_per[idx - 1] + time_per[idx]

print(sum(time_per))