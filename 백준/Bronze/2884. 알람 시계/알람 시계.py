import sys
input = sys.stdin.readline

H, M = map(int, input().split())
H = ((H - 1) if M < 45 else H) % 24
M = (M - 45) % 60


print(H, M)