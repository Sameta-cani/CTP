N, M = map(int, input().split())

array = list(range(N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    array[i], array[j] = array[j], array[i]
    
print(*array[1:])