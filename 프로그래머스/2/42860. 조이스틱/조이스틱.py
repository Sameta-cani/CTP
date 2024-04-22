def solution(name):
    spell_move = 0
    
    cursor_move = len(name) - 1
    
    for index, ch in enumerate(name):
        spell_move += min(ord(ch) - ord('A'), ord('Z') - ord(ch) + 1)
        
        next = index + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        cursor_move = min([cursor_move, 2 * index + len(name) - next, index + 2 * (len(name) - next)])
        
    return spell_move + cursor_move