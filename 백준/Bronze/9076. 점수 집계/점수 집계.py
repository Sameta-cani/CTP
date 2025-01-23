import sys

input = sys.stdin.readline

for _ in range(int(input())):
    scores = sorted(list(map(int, input().split())))[1:-1]
    if (scores[-1] - scores[0]) >= 4:
        print("KIN")
    else:
        print(sum(scores))