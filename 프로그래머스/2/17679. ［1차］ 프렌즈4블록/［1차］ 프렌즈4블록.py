def updating(m: int, n: int, board: list) -> tuple:
    # 2차원 리스트로 변환
    tmp = [list(row) for row in board]
    
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    # 지워질 블록의 위치를 담을 set
    target = set()
    
    for row in range(m-1):
        for col in range(n-1):
            base = tmp[row][col]
            if base == '-':
                continue
            # base 기준 4칸 모두 같으면 target에 해당 위치 전부 추가
            if all(tmp[row + x][col + y] == base for x, y in zip(dx, dy)):
                target.update((row + x, col + y) for x ,y in zip([0] + dx, [0] + dy))
                
    # 타겟이 된 위치를 '-'로 변경
    for r, c in target:
        tmp[r][c] = '-'
        
    # 각 열에 접근하여 '-'를 제거하고 문자를 아래로 이동
    for col in range(n):
        stack = [tmp[row][col] for row in range(m) if tmp[row][col] != '-']
        for row in range(m-1, -1, -1):
            tmp[row][col] = stack.pop() if stack else '-'
            
    return tmp, target

def solution(m: int, n: int, board: list) -> int:
    while True:
        board, target = updating(m, n, board)
        # 업데이트 하면서 사라질 블록이 없으면 끝
        if not target:
            break
    
    # 지워진 블록('-')의 개수 카운트
    res = sum(row.count('-') for row in board)
    return res