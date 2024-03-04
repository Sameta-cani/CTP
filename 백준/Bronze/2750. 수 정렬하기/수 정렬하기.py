# 선택 정렬

N = int(input())
data = [int(input()) for _ in range(N)]

for i in range(len(data)):
    min_index = i
    for j in range(i + 1, len(data)):
        if data[min_index] > data[j]:
            min_index = j
    data[i], data[min_index] = data[min_index], data[i]

print(*data, sep='\n')