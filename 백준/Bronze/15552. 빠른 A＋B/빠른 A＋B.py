import sys

# 테스트 케이스의 개수 T 입력
T = int(sys.stdin.readline().rstrip())

# T만큼 입력
for i in range(T):
  # 두 정수 A와 B 입력
  A, B = map(int, sys.stdin.readline().split())
  # 합 출력
  sys.stdout.write(str(A+B)+'\n')