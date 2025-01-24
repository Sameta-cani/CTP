import sys

input = sys.stdin.readline

def binary_search(X, target_vs, start, end, my_v):
    target = X / target_vs
    result = -1
    while start <= end:
        mid = (start + end) // 2
        total = (X - mid) / my_v + 1
        
        if total < target:
            end = mid - 1
            result = mid
        else:
            start = mid + 1

    return result
        


for _ in range(int(input())):
    N, X, Y = map(int, input().split())
    Vs = list(map(int, input().split()))
    
    target_vs, my_v = max(Vs[:-1]), Vs[-1]
    if my_v > target_vs:
        print(0)
        continue
    
    if X / target_vs <= (X - Y) / my_v + 1:
        print(-1)
        continue
    
    Z = binary_search(X, target_vs, 0, Y, my_v)
    print(Z)