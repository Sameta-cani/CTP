def solution(n, lost, reserve):
    array = [1] * n
    
    for index in range(n):
        if index + 1 in lost:
            array[index] -= 1
        if index + 1 in reserve:
            array[index] += 1
    
    for i in range(n):
        if array[i] == 0:
            if i > 0 and array[i - 1] == 2:
                array[i - 1] -= 1
                array[i] += 1
            elif i < n - 1 and array[i + 1] == 2:
                array[i + 1] -= 1
                array[i] += 1
    
    answer = sum(1 for x in array if x >= 1)
    
    return answer