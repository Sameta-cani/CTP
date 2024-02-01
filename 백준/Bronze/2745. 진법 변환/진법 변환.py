import sys

N, B = sys.stdin.readline().rstrip().split()
result = 0

for ind, val in enumerate(N):
    if 48 <= ord(val) <= 57:
        val = int(val)
    else:
        val = ord(val) - 55

    result += val * int(B) ** (len(N) - ind - 1)

print(result) # int(N, int(B))도 가능