def solution(number: int, n: int, m: int) -> int:
    answer = int(not(number % n) and not(number % m))
    return answer