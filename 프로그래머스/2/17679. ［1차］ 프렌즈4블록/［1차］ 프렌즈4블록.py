def updating(m: int, n: int, board: list):
    tmp = [list(row) for row in board]
    
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    target = set()
    
    # 2x2 블록의 일치를 검사합니다.
    for row in range(m-1):
        for col in range(n-1):
            base = tmp[row][col]
            if base == '-':
                continue
            if all(tmp[row + x][col + y] == base for x, y in zip(dx, dy)):
                target.update((row + x, col + y) for x, y in zip([0] + dx, [0] + dy))
                
    # 타겟이 된 위치를 '-'로 변경합니다.
    for r, c in target:
        tmp[r][c] = '-'
    
    # 각 열을 처리하여 '-'를 제거하고 문자를 아래로 이동시킵니다.
    for col in range(n):
        stack = [tmp[row][col] for row in range(m) if tmp[row][col] != '-']
        for row in range(m-1, -1, -1):
            tmp[row][col] = stack.pop() if stack else '-'
    
    return tmp, target

def solution(m: int, n: int, board: list) -> int:
    while True:
        board, c = updating(m, n, board)
        if not c:
            break
    
    # '-'의 개수를 셉니다.
    res = sum(row.count('-') for row in board)
    return res