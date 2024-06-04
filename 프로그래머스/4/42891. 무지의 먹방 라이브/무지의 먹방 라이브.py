def solution(food_times: list, k: int) -> int:
    if sum(food_times) <= k:
        return -1
    
    sorted_food_times = sorted([(time, idx) for idx, time in enumerate(food_times)])
    length = len(food_times)
    
    prev_time = 0
    for i, (time, idx) in enumerate(sorted_food_times):
        time_to_eat = (time - prev_time) * length
        
        if k >= time_to_eat:
            k -= time_to_eat
            prev_time = time
        else:
            k %= length
            remaining_foods = sorted(sorted_food_times[i:], key=lambda x: x[1])
            return remaining_foods[k][1] + 1
        
        length -= 1
    
    return -1