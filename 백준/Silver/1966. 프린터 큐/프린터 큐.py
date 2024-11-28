from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    weights = deque(list())
    for idx, val in enumerate(list(map(int, input().split()))):
        weights.append((val, idx))
    cnt = 0
    while weights:
        cur = weights[0][0]
        rotate_cnt = weights.index(max(weights, key=lambda x: x[0]))
        cnt += 1
        weights.rotate(-rotate_cnt)
        if weights[0][1] == M:
            break
        weights.popleft()
    
    print(cnt)
