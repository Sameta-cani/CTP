import sys

input = sys.stdin.readline

def solution(n: int) -> int:
    return sum([val for val in range(2, n + 1, 2)])