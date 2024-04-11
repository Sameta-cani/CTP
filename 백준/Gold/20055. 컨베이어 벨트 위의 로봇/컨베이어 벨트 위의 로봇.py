from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

conveyor = deque(list(map(int, input().split())))
robot = deque([False] * N)
step = 1

while True:
    conveyor.appendleft(conveyor.pop())
    robot.appendleft(robot.pop())
    if robot[N - 1] == True:
        robot[N - 1] = False

    for i in range(N - 2, -1, -1):
        if robot[i] == True and not robot[i + 1] and conveyor[i + 1] >= 1:
            conveyor[i + 1] -= 1
            robot[i + 1] = True
            robot[i] = False

    robot[-1] = False

    if conveyor[0] > 0 and not robot[0]:
        conveyor[0] -= 1
        robot[0] = True

    if conveyor.count(0) >= K:
        break
    step += 1

print(step)