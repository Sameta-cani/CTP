def solution(id_list: list, report: list, k: int) -> list:
    answer = [0] * len(id_list)
    cumulative_reports = {name: 0 for name in id_list}
    
    for data in set(report):
        cumulative_reports[data.split()[1]] += 1
        
    for data in set(report):
        if cumulative_reports[data.split()[1]] >= k:
            answer[id_list.index(data.split()[0])] += 1
            
    return answer