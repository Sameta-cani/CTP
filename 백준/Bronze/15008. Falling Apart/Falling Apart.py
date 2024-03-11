n = int(input())
array = sorted(list(map(int, input().split())), reverse=True)

Alice = array[0:len(array):2]
Bob = array[1:len(array):2]

print(sum(Alice), sum(Bob))