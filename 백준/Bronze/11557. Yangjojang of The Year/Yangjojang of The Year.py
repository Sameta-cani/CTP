T = int(input())

for _ in range(T):
    N = int(input())
    array = sorted([tuple(input().split()) for _ in range(N)], key=lambda x: int(x[1]), reverse=True)
    print(array[0][0])