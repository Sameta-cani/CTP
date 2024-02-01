import sys

N = int(sys.stdin.readline().rstrip())

points = 4 # 초기 점의 수

for i in range(1, N+1):
    points = points * 4 - (3 + 2**(i+1))

print(points) # points = (2**N+1)**2
