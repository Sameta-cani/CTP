import sys

def insertion_sort(array, limit):
    count = 0
    for i in range(1, len(array)):
        loc = i - 1
        newItem = array[i]

        while (0 <= loc and newItem < array[loc]):
            count += 1
            if count == limit:
                return array[loc]
            array[loc + 1] = array[loc]
            loc -= 1

        if loc + 1 != i:
            count += 1
            if count == limit:
                return newItem
            array[loc + 1] = newItem
    return -1

N, K = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))


print(insertion_sort(array, K))