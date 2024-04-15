import sys
import math

input = sys.stdin.readline

N = int(input()) # 파일의 개수
file_size = list(map(int, input().split())) # 파일의 크기
cluster_size = int(input()) # 클러스터의 크기

count = 0 # 필요한 클러스터의 개수 초기화

for file in file_size:
    count += math.ceil(file / cluster_size)

print(count * cluster_size)