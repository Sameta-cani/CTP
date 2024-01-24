import sys

not_submitted = [True] * 30

for _ in range(28):
    n = int(sys.stdin.readline().rstrip())
    not_submitted[n-1] = False

print(*[i + 1 for i, submitted in enumerate(not_submitted) if submitted], sep='\n')