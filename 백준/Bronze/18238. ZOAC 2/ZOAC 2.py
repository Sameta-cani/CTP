import sys

input = sys.stdin.readline

sent = input().rstrip()

res = 0
start = ord('A')
for alpha in sent:
    left = (ord(alpha) - start) % 26
    right = (start - ord(alpha)) % 26

    res += min(left, right)
    start = ord(alpha)

print(res)