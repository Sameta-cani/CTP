from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    weights = deque(enumerate(map(int, input().split())))
    cnt = 0

    while weights:
        rotate_cnt = weights.index(max(weights, key=lambda x: x[1]))
        weights.rotate(-rotate_cnt)
        cnt += 1  
        if weights[0][0] == M:
            break
        weights.popleft()
    
    print(cnt)