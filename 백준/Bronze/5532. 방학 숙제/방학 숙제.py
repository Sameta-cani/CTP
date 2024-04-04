import math

L = int(input()) # 총 방학 기간
A = int(input()) # 전체 국어 페이지
B = int(input()) # 전체 수학 페이지
C = int(input()) # 하루에 풀 수 있는 국어
D = int(input()) # 하루에 풀 수 있는 수학

print(L - max(math.ceil(B / D), math.ceil(A / C)))