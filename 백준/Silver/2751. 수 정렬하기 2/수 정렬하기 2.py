import sys
import heapq

def heapsort(iterable):
    h, result = [], []
    for value in iterable:
        heapq.heappush(h, value)
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result

N = int(sys.stdin.readline().rstrip())
array = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

print(*heapsort(array), sep='\n')