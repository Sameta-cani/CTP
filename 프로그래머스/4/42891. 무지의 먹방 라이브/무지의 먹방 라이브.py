def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    # 음식 시간을 (음식 시간, 인덱스)의 형태로 정렬
    sorted_food_times = sorted([(time, idx) for idx, time in enumerate(food_times)])
    length = len(food_times)
    
    previous_time = 0
    for i, (time, idx) in enumerate(sorted_food_times):
        # 현재 음식에서 시간을 다 먹을 때까지의 시간 계산
        time_to_eat = (time - previous_time) * length
        
        if k >= time_to_eat:
            k -= time_to_eat
            previous_time = time
        else:
            k %= length
            # 원래 인덱스 기준으로 정렬된 남은 음식들을 구함
            remaining_foods = sorted(sorted_food_times[i:], key=lambda x: x[1])
            return remaining_foods[k][1] + 1
        
        length -= 1
    
    return -1