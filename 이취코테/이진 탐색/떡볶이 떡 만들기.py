import sys

input = sys.stdin.readline

# Read the number of rice cakes (N) and the requested total length (M)
N, M = map(int, input().split())
# Read the heights of each rice cake
array = list(map(int, input().split()))

# Init binary search boundaries
start, end = 0, max(array)

# Perform binary search
result = 0
while start <= end:
    mid = (start + end) // 2
    # Calculate the total length of rice cakes that would be cut off at the current mid height
    total = sum(val - mid for val in array if val > mid)
    
    # If the total length is less than the requested amount, move the end to mid - 1
    if total < M:
        end = mid - 1
    else:
        # If the total length is sufficient, store the current mid as the potential result
        result = mid
        start = mid + 1
        
# Print the final result
print(result)