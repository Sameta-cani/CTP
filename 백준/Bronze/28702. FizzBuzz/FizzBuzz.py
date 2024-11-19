ans = None

for idx in range(3):
    word = input()
    if word.isdigit():
        ans = int(word) + (3 - idx)

if ans:
    if ans % 15 == 0:
        print("FizzBuzz")
    elif ans % 3 == 0:
        print("Fizz")
    elif ans % 5 == 0:
        print("Buzz")
    else:
        print(ans)
