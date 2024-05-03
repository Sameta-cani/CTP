import sys

input = sys.stdin.readline

def generate_lucky_numbers(limit):
    lucky_numbers = []

    def backtrack(number):
        if number > limit:
            return
        if number > 0:
            lucky_numbers.append(number)
        backtrack(number * 10 + 4)
        backtrack(number * 10 + 7)

    backtrack(0)
    return sorted(lucky_numbers)


def find_largest_lucky_number(n):
    lucky_numbers = generate_lucky_numbers(n)
    return max(lucky_numbers) if lucky_numbers else -1

N = int(input())

print(find_largest_lucky_number(N))