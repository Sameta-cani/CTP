import sys

input = sys.stdin.readline

N, K = map(int, input().split())
result = 0

# N이 K 이상이라면 K로 계속 나누기
while N >= K:
    # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
    while N % K != 0:
        N -= 1
        result += 1
    # K로 나누기
    N //= K
    result += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while N > 1:
    N -= 1
    result += 1

print(result)