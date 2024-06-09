import sys

input = sys.stdin.readline

def solution(angle: int) -> int:
    if angle == 180:
        return 4
    elif angle == 90:
        return 2
    
    if 0 < angle < 90:
        return 1
    elif 90 < angle < 180:
        return 3