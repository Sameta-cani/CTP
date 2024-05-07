import sys

input = sys.stdin.readline

N, M = map(int, input().split())

memo = set(input().rstrip() for _ in range(N))
keywords = [tuple(input().rstrip().split(',')) for _ in range(M)]

for keyword in keywords:
   for key in keyword:
      if key not in memo:
         continue
      else:
         memo.remove(key)
   print(len(memo))