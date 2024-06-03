def updating(m: int, n: int, board: list) -> tuple:
    tmp = [list(row) for row in board]
    
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    target = set()
    
    for row in range(m-1):
        for col in range(n-1):
            base = tmp[row][col]
            if base == '-':
                continue
            if all(tmp[row + x][col + y] == base for x, y in zip(dx, dy)):
                target.update((row + x, col + y) for x ,y in zip([0] + dx, [0] + dy))
                
    for r, c in target:
        tmp[r][c] = '-'
        
    for col in range(n):
        stack = [tmp[row][col] for row in range(m) if tmp[row][col] != '-']
        for row in range(m-1, -1, -1):
            tmp[row][col] = stack.pop() if stack else '-'
            
    return tmp, target

def solution(m: int, n: int, board: list) -> int:
    while True:
        board, target = updating(m, n, board)
        if not target:
            break
        
    res = sum(row.count('-') for row in board)
    return res