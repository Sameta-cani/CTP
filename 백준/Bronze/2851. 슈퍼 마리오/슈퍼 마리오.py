import sys

input = sys.stdin.readline

diff = float('inf')
tmp = 0

for _ in range(10):
    n = int(input())
    tmp += n
    
    if abs(100 - tmp) <= diff:
        diff = abs(100 - tmp)
        ans = tmp

print(ans)