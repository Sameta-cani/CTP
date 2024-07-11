def solution(a: int, b: int) -> int:
    answer = max(int(f'{a}{b}'), 2 * a * b)
    return answer