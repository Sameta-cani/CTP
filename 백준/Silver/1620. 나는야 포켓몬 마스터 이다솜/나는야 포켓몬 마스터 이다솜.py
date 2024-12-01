import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ency_to_name = {}
name_to_ency = {}

for idx in range(1, N + 1):
    name = input().strip()
    ency_to_name[idx] = name
    name_to_ency[name] = idx

for _ in range(M):
    prob = input().strip()
    if prob.isdigit():
        print(ency_to_name[int(prob)])
    else:
        print(name_to_ency[prob])
