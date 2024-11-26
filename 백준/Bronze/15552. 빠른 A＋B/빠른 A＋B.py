import sys
input = sys.stdin.readline

for _ in range(int(input())):
    sys.stdout.write(str(sum(map(int, input().split())))+'\n')