import sys
input = sys.stdin.readline

max_value = int(-1e9)
N = 0

for _ in range(4):
    # 내린 사람, 탑승한 사람
    a, b = map(int, input().split())
    # 역 최종 사람
    N = N - a + b
    # 가장 큰 값 갱신
    max_value = max(max_value, N)

print(max_value)