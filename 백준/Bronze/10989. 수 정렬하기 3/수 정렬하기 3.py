import sys
input = sys.stdin.readline

cnt = [0] * 10001

for _ in range(int(input())):
    cnt[int(input())] += 1

for idx in range(1, 10001):
    if cnt[idx]:
        for _ in range(cnt[idx]):
            print(idx)