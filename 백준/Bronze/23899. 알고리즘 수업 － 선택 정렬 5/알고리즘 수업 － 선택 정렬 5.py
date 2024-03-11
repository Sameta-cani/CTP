import sys

def selection_sort(A, B):
    if A == B:
        return 1
    for i in range(len(A)-1, 0, -1):
        max_index = i
        for j in range(i + 1):
            if A[max_index] < A[j]:
                max_index = j

        if i != max_index:
            A[max_index], A[i] = A[i], A[max_index]
            if A == B:
                return 1
    return 0

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list((map(int, sys.stdin.readline().rstrip().split())))

print(selection_sort(A, B))