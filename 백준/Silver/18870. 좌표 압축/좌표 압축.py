import sys

N = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))

sort_array = sorted(set(array))

index_dict = {value: i for i, value in enumerate(sort_array)}

for value in array:
    sys.stdout.write(f'{index_dict[value]} ')