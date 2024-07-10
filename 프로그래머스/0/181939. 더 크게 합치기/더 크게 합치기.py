def solution(a, b):
    answer = int(max(f"{a}{b}", f"{b}{a}"))
    return answer