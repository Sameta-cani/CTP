import sys

input = sys.stdin.readline

def solution(my_string: str, letter: str) -> str:
    return my_string.replace(letter, '')