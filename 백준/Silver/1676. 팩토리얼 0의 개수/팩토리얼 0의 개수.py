N = int(input())

# Count the number of factors of 5 in N!
count = 0
power_of_5 = 5
while N >= power_of_5:
    count += N // power_of_5
    power_of_5 *= 5

print(count)