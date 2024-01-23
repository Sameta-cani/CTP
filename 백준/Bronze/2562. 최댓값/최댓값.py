import sys

max_value = float("-inf")
max_ind = 0

for ind in range(1, 10):
    val = int(sys.stdin.readline().rstrip())
    if val > max_value:
        max_value = val
        max_ind = ind

print(max_value, max_ind, sep='\n')