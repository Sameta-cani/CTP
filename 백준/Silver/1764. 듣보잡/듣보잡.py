import sys
input = sys.stdin.readline

N, M = map(int, input().split())

heard = {input().strip() for _ in range(N)}
seen = {input().strip() for _ in range(M)}

res = sorted(heard & seen)

print(len(res))
print("\n".join(res))