def solution(ineq: str, eq: str, n: int, m: int) -> int:
    answer = 0
    if ineq  == '<':
        if eq == '=':
            answer = 1 if n <= m else 0
        elif eq == '!':
            answer = 1 if n < m  else 0
    elif ineq == '>':
        if eq == '=':
            answer = 1 if n >= m else 0
        elif eq == '!':
            answer = 1 if n > m else 0
    return answer