def solution(new_id: str):
    answer = ''
    tmp = new_id.lower()
    allowed_list = ['-', '_', '.']
    prev = ''
    for ch in tmp:
        if ch.isalpha() or ch.isalnum() or ch in allowed_list:
            if prev != '.' and ch == '.':
                prev = ch
            elif prev == '.' and ch == '.':
                continue
            answer += ch
            prev = ch
            
    answer = answer.strip('.')
    if not answer:
        answer = 'a'
    answer = answer[:15].rstrip('.')
    while len(answer) <= 2:
        answer += answer[-1]
        
    return answer