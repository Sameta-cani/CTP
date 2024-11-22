import heapq
import sys
input = sys.stdin.readline

def heapsort(iterable):
    heapq.heapify(iterable)
    while iterable:
        yield heapq.heappop(iterable)

data = [int(input()) for _ in range(int(input()))]

for num in heapsort(data):
    print(num)