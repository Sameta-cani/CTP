from collections import deque

def solution(queue1, queue2):
    total_queue = deque(queue1 + queue2)
    total_sum = sum(total_queue)
    if total_sum % 2 != 0:
        return -1 
    
    target = total_sum // 2
    current_sum = sum(queue1) 
    min_op = 0
    i, j = 0, len(queue1)  

    while i < len(total_queue):
        if current_sum == target:
            return min_op
        
        if current_sum < target:
            if j < len(total_queue): 
                current_sum += total_queue[j]
                j += 1
            else:
                break 
        else: 
            current_sum -= total_queue[i]
            i += 1
        min_op += 1

    return -1