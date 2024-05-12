def del_dot(id: str):
    if id.startswith('.'):
        id = id[1:]
    if id.endswith('.'):
        id = id[:-1]
        
    return id


def solution(new_id: str):
    answer = ''
    tmp = new_id.lower()
    permit_list = ['-', '_', '.']
    prev = ''
    for ch in tmp:
        if ch.isalpha() or ch.isalnum() or ch in permit_list:
            if prev != '.' and ch == '.':
                prev = ch
            elif prev == '.' and ch == '.':
                continue
            answer += ch
            prev = ch
            
    answer = del_dot(answer)
    if answer == '':
        answer = 'a'
    answer = answer[:15]
    answer = del_dot(answer)
    while len(answer) <= 2:
        end_alpha = answer[-1]
        answer += end_alpha
    return answer