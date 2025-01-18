msg = "WelcomeToSMUPC"

N = int(input())

print(msg[(N - 1) % len(msg)])