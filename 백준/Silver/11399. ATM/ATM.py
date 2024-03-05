import sys

N = int(input())

array = list(map(int, sys.stdin.readline().rstrip().split()))
array.sort()

prev_time = array[0]
total_time = array[0]

for time in array[1:]:
    time += prev_time
    total_time += time
    prev_time = time
    
print(total_time)