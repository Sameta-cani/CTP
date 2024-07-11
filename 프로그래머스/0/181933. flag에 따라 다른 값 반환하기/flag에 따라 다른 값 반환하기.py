def solution(a: int, b: int, flag: bool) -> int:
    answer = a + b if flag else a - b
    return answer