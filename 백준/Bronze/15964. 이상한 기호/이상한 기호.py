def cal(A, B):
    return (A + B) * (A - B)

A, B = map(int, input().split())

print(cal(A, B))