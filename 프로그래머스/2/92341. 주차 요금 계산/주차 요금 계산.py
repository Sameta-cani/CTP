from collections import defaultdict
from math import ceil

def solution(fees: list, records: list) -> list:
    tmp = []
    default_time, default_fee = fees[0], fees[1]
    unit_time, unit_fee = fees[2], fees[3]
    
    info = dict()
    fee_dict = defaultdict(int)
    
    for record in records:
        time, number, state = record.split()
        if state == "IN":
            info[number] = time
        elif state == "OUT":
            # 요금 처리 알고리즘
            in_hour, in_min = map(int, info[number].split(':'))
            out_hour, out_min = map(int, time.split(':'))
            del_time = (out_hour * 60 + out_min) - (in_hour * 60 + in_min)
            fee_dict[number] += del_time
            del info[number]
    
    if info:
        for k, v in info.items():
            in_hour, in_min = map(int, v.split(':'))
            del_time = (23 * 60 + 59) - (in_hour * 60 + in_min)
            fee_dict[k] += del_time      
    del info

    for k, v in fee_dict.items():
        fee_dict[k] = default_fee + ceil((v - default_time) / unit_time) * unit_fee if v > default_time else default_fee
        tmp.append((k, fee_dict[k]))
        
    tmp.sort(key=lambda x: x[0])
    answer = [v[1] for v in tmp]
    return answer