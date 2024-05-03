import sys

input = sys.stdin.readline

N = int(input())

data = []

def backtrack(data, num):
    if num > N:
        return
    if num > 0:
        data.append(num)
    backtrack(data, num * 10 + 4)
    backtrack(data, num * 10 + 7)

backtrack(data, 0)
print(max(data))