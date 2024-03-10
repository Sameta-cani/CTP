def selection_sort(array, limit):
    count = 0
    for last in range(len(array)-1, 0, -1):
        max_index = last
        for i in range(last+1):
            if array[max_index] < array[i]:
                max_index = i
        if last != max_index:
            count += 1
            array[max_index], array[last] = array[last], array[max_index]
        
        if count == limit:
            print(*array)
            return
    print(-1)


N, K = map(int, input().split())
array = list(map(int, input().split()))

selection_sort(array, K)