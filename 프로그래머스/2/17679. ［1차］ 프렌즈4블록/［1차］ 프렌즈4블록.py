def updating(m: int, n: int, board: list):
    tmp = [list(row) for row in board]
    
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    target = set()
    
    for row in range(m-1):
        for col in range(n-1):
            base = tmp[row][col]
            if base == '-':
                continue
            is_same = all(tmp[row + x][col + y] == base for x, y in zip(dx, dy))
            if is_same:
                target.update((row + x, col + y) for x, y in zip([0] + dx, [0] + dy))
                
    for r, c in target:
        tmp[r][c] = '-'
            
    for col in range(n):
        stack = []
        for row in range(m):
            if tmp[row][col] != '-':
                stack.append(tmp[row][col])
                    
        for row in range(m-1, -1, -1):
            if stack:
                tmp[row][col] = stack.pop()
            else:
                tmp[row][col] = '-'
                    
    return tmp, target

def solution(m: int, n: int, board: list) -> int:
    while True:
        board, c = updating(m, n, board)
        if not c:
            res = 0
            for row in range(m):
                for col in range(n):
                    if board[row][col] == '-':
                        res += 1
            break
    
    return res