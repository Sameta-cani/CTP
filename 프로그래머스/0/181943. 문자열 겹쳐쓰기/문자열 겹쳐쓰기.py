def solution(my_string: str, overwrite_string: str, s: int) -> str:
    answer = my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]
    return answer