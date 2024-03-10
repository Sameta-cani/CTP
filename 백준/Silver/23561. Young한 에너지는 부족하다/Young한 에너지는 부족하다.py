N = int(input())

array = list(map(int, input().split()))

array.sort()

print(array[2*N-1] - array[N])