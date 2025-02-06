from collections import deque
import sys

input = sys.stdin.readline

def direction_change(d: int, c: str) -> int:
    return (d + 1) % 4 if c == 'L' else (d - 1) % 4

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

N = int(input())
K = int(input())

board = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    x, y = map(int, input().split())
    board[x][y] = 1
    
times = {}
for _ in range(int(input())):
    X, C = input().split()
    times[int(X)] = C
    
direction = 0
time = 0
x, y = 1, 1
snake = deque([(x, y)])
board[x][y] = 2

while True:
    time += 1
    nx, ny = x + dx[direction], y + dy[direction]

    if not (1 <= nx <= N and 1 <= ny <= N) or board[nx][ny] == 2:
        break
    
    if board[nx][ny] == 1:
        board[x][y] = 2
    else:
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0
        
    snake.append((nx, ny))
    board[nx][ny] = 2
    
    if time in times:
        direction = direction_change(direction, times[time])
        
    x, y = nx, ny
    
print(time)