from typing import List
import math

def solution(num_list: List[int]) -> int:
    answer = 1 if math.prod(num_list) < sum(num_list)**2 else 0
    return answer