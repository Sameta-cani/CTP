import sys

def insertion_sort(array, limit):
    count = 0
    for i in range(1, len(array)):
        loc = i - 1
        newItem = array[i]

        while (0 <= loc and newItem < array[loc]):
            count += 1
            array[loc + 1] = array[loc]
            loc -= 1
            if count == limit:
                return array

        if (loc + 1) != i:
            count += 1
            array[loc + 1] = newItem
            if count == limit:
                return array
            
    return [-1]

N, K = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

print(*insertion_sort(array, K))