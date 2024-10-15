import sys

for val in sys.stdin:
    print(sum(map(int, val.split())))