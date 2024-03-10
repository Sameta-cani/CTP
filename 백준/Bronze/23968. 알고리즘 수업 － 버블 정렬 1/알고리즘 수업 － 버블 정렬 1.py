import sys

def bubble_sort(array, limit):
    count = 0
    for last in range(len(array)-1, 0, -1):
        for i in range(last):
            if array[i] > array[i + 1]:
                count += 1
                if count == limit:
                    return array[i], array[i + 1]
                array[i], array[i + 1] = array[i + 1], array[i]
    return -1

N, K = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

result = bubble_sort(array, K)

if type(result) == int:
    print(result)
else:
    print(*(sorted(result)))