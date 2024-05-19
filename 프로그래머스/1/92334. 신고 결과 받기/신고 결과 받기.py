from collections import defaultdict

def solution(id_list: list, report: list, k: int) -> list:
    tmp = {name: 0 for name in id_list}
    report_status = defaultdict(list) # 사용자가 신고한 유저 목록
    cumulative_report = defaultdict(int) # 누적 신고 수
    for data in set(report):
        a, b = data.split()
        report_status[a].append(b)
        cumulative_report[b] += 1
    
    for ik, v in report_status.items():
        for name in v:
            if name in cumulative_report and cumulative_report[name] >= k:
                tmp[ik] += 1
    
    answer = [v for v in tmp.values()]
    return answer