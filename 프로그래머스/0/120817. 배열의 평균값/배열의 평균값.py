import sys

input = sys.stdin.readline

def solution(numbers: list) -> float:
    return sum(numbers) / len(numbers)