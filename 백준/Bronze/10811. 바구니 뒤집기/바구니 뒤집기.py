N, M = map(int, input().split())

array = list(range(N + 1))
for _ in range(M):
    i, j = map(int, input().split())
    array[i:j + 1] = array[i:j + 1][::-1]
        
print(*array[1:])
