from typing import List

def solution(a: int, b: int, included: List[bool]) -> int:
    answer = 0
    for n in range(1, len(included) + 1):
        val = a + (n - 1) * b
        answer += val if included[n - 1] else 0
    return answer