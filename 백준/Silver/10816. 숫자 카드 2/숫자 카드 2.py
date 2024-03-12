from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

N = int(input().rstrip())
array = sorted(list(map(int, input().rstrip().split())))
M = int(input().rstrip())


for val in list(map(int, input().rstrip().split())):
    print(count_by_range(array, val, val), end=' ')