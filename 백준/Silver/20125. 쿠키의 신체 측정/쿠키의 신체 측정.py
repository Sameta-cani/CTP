import sys

input = sys.stdin.readline

N = int(input())
board = [input().rstrip() for _ in range(N)]

head_exist = False
heart_pos = (0, 0)
ans = [0] * 5 # 왼쪽 팔, 오른쪽 팔, 허리, 왼쪽 다리, 오른쪽 다리
for c in range(N):
    for r in range(N):
        if board[c][r] == '*':
            # 심장
            if not head_exist:
                head_exist = True
                heart_pos = (c + 2, r + 1)
            # 왼쪽 팔
            if c + 1 == heart_pos[0] and r + 1 < heart_pos[1]:
                ans[0] += 1
            # 오른쪽 팔
            elif c + 1 == heart_pos[0] and r + 1 > heart_pos[1]:
                ans[1] += 1
            # 허리
            elif c + 1 > heart_pos[0] and r + 1 == heart_pos[1]:
                ans[2] += 1
            # 왼쪽 다리
            elif c + 1 > heart_pos[0] and r + 1 < heart_pos[1]:
                ans[3] += 1
            # 오른쪽 다리
            elif c + 1 > heart_pos[0] and r + 1 > heart_pos[1]:
                ans[4] += 1
      
print(*heart_pos)
print(*ans)