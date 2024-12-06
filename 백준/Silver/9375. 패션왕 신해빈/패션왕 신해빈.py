from collections import defaultdict
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    cloth_cnt = defaultdict(int)

    for _ in range(int(input())):
        _, cloth_type = input().strip().split()
        cloth_cnt[cloth_type] += 1
    
    res = 1
    for count in cloth_cnt.values():
        res *= (count + 1)

    print(res - 1)