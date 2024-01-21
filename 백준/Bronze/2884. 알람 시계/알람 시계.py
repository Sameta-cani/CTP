import sys

h, m = map(int, sys.stdin.readline().rstrip().split())

new_h = (h - (m < 45)) % 24
new_m = (m - 45) % 60

print(new_h, new_m)
