from collections import Counter
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

array = []
for _ in range(1, N + 1):
    data = list(map(int, input().split()))
    nth, info = data[0], data[1:]
    if nth == K:
        main = ''.join(map(str, info))
    array.append(''.join(map(str, info)))

array.sort(reverse=True)
count = Counter(array)


ans = 0
for idx in range(array.index(main)):
    ans += count.get(array[idx])
print(ans + 1)