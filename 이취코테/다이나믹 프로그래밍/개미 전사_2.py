import sys

input = sys.stdin.readline

# Read the integer N
N = int(input())
# Read the list of food amounts
array = list(map(int, input().split()))

# Edge cases for small N
if N == 0:
    print(0)
    exit()
elif N == 1:
    print(array[0])
    exit()
    
# Init the first two values for the dynamic programming approach
prev2 = array[0]
prev1 = max(array[0], array[1])

# Process the rest of the array
for idx in range(2, N):
    current = max(prev1, prev2 + array[idx])
    prev2 = prev1
    prev1 = current
    
# The result is in prev1
print(prev1)