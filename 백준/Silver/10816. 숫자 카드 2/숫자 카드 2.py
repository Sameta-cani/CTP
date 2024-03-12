from bisect import bisect_left, bisect_right
import sys

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

N = int(sys.stdin.readline().rstrip())
array = sorted(list(map(int, sys.stdin.readline().rstrip().split())))
M = int(sys.stdin.readline().rstrip())


for val in list(map(int, sys.stdin.readline().rstrip().split())):
    print(count_by_range(array, val, val), end=' ')