import sys

input = sys.stdin.readline

company = dict()
for _ in range(int(input())):
    name, state = input().split()

    if state == "enter":
        company[name] = True
    else:
        del company[name]
    
for name in sorted(company.keys(), reverse=True):
    print(name)