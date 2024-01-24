import sys

N = int(sys.stdin.readline().rstrip())

for i in range(1, 2 * N):
    # 마름모 위쪽 및 아래쪽을 통합한 로직
    stars = (N - abs(N - i)) * 2 - 1
    spaces = abs(N - i)
    print(' ' * spaces + '*' * stars)
