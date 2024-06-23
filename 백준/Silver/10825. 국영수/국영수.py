import sys

input = sys.stdin.readline

N = int(input())

data = []
for _ in range(N):
    info = input().rstrip().split()
    data.append((-int(info[1]), int(info[2]), -int(info[3]), info[0]))
    
data.sort(reverse=False)

for value in data:
    print(value[3])