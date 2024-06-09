import sys

input = sys.stdin.readline

def solution(array: list, height: int) -> int:
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)