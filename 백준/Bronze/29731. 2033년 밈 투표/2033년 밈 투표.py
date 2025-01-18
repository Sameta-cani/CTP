base = [
    "Never gonna give you up",
    "Never gonna let you down",
    "Never gonna run around and desert you",
    "Never gonna make you cry",
    "Never gonna say goodbye",
    "Never gonna tell a lie and hurt you",
    "Never gonna stop",
]

is_accept = False
for _ in range(int(input())):
    sen = input().strip()
    if sen not in base:
        is_accept = True
        
print("Yes" if is_accept else "No")