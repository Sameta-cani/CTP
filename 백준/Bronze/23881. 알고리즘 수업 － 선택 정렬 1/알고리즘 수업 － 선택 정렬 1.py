def selection_sort(array, limit):
    count = 0
    for last in range(len(array)-1, -1, -1):
        max_index = last
        for i in range(last + 1):
            if array[i] > array[max_index]:
                max_index = i
        if last != max_index:
            array[last], array[max_index] = array[max_index], array[last]
            count += 1
        if count == limit:
            return array[last], array[max_index]
    return -1

N, K = map(int, input().split())
array = list(map(int, input().split()))
answer = selection_sort(array, K)

if type(answer) == int:
    print(answer)
else:
    print(*sorted(answer))