def solution(routes):
    routes.sort(key=lambda x: x[1])
    
    answer = 0
    current = float('-inf')
    
    for route in routes:
        if current < route[0]:
            answer += 1
            current = route[1]
            
    return answer