import math

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    # 조합의 공식을 사용하여 경우의 수를 계산
    result = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))
    print(result)
