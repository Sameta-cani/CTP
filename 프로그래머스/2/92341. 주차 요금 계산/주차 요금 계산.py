from collections import defaultdict
from math import ceil

def solution(fees: list, records: list) -> list:
    default_time, default_fee = fees[0], fees[1]
    unit_time, unit_fee = fees[2], fees[3]
    
    info = dict()
    fee_dict = defaultdict(int)
    
    for record in records:
        time, number, state = record.split()
        if state == "IN":
            info[number] = time
            if number not in fee_dict:
                fee_dict[number] = 0
        elif state == "OUT":
            in_hour, in_min = map(int, info[number].split(':'))
            out_hour, out_min = map(int, time.split(':'))
            del_time = (out_hour * 60 + out_min) - (in_hour * 60 + in_min)
            fee_dict[number] += del_time
            del info[number]
    
    for k in fee_dict.keys():
        if k in info:
            in_hour, in_min = map(int, info[k].split(':'))
            del_time = (23 * 60 + 59) - (in_hour * 60 + in_min)
            fee_dict[k] += del_time
            del info[k]
            
        total_time = fee_dict[k]
        
        fee_dict[k] = default_fee + ceil((total_time - default_time) / unit_time) * unit_fee if total_time > default_time else default_fee
    
    answer = [values[1] for values in sorted(fee_dict.items())]
    return answer