from collections import defaultdict
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

site_dict = defaultdict(str)
for _ in range(N):
    site_info = input().rstrip().split()
    site_dict[site_info[0]] = site_info[1]    

targets = [site_dict.get(input().strip()) for _ in range(M)]

print(*targets, sep='\n')